import os
import shutil
import platform
from pathlib import Path
from mnds_cui import mnds_ascii_art

# --- 設定 ---
CUSTOM_CURSORS_DIR = Path("custom_cursors")
BACKUP_DIR_NAME = "cursors_backup"
STATE_FILE_NAME = ".cursor_state"  # 状態を記録する隠しファイル

def get_default_hoi4_path():
    sys_name = platform.system()
    if sys_name == "Windows":
        return Path("C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV")
    elif sys_name == "Darwin":
        return Path.home() / "Library/Application Support/Steam/steamapps/common/Hearts of Iron IV"
    elif sys_name == "Linux":
        return Path.home() / ".local/share/Steam/steamapps/common/Hearts of Iron IV"
    return None

def verify_hoi4_path(path: Path) -> bool:
    if not path.exists() or not path.is_dir():
        return False
    return (path / "gfx" / "cursors").exists()

# --- ステート管理関数 ---
def get_current_state(hoi4_path: Path) -> str:
    """現在の状態を読み取る。ファイルがない場合は 'VANILLA' とみなす"""
    state_file = hoi4_path / "gfx" / STATE_FILE_NAME
    if state_file.exists():
        with open(state_file, "r", encoding="utf-8") as f:
            return f.read().strip()
    return "VANILLA"

def set_current_state(hoi4_path: Path, state: str):
    """現在の状態をファイルに書き込む"""
    state_file = hoi4_path / "gfx" / STATE_FILE_NAME
    with open(state_file, "w", encoding="utf-8") as f:
        f.write(state)

# --- コアロジック ---
def setup_backup(hoi4_path: Path):
    cursors_dir = hoi4_path / "gfx" / "cursors"
    backup_dir = hoi4_path / "gfx" / BACKUP_DIR_NAME
    current_state = get_current_state(hoi4_path)
    
    # 【重要】現在の状態がバニラであることが確定している時のみバックアップを作成
    if current_state == "VANILLA":
        if not backup_dir.exists():
            print("[*] 現在バニラ環境です。最新のクリーンなバックアップを作成します...")
            shutil.copytree(cursors_dir, backup_dir)
            print("[+] バックアップ完了。")
    else:
        if not backup_dir.exists():
            print("[!] 重大エラー: カスタム状態ですが、バックアップが見つかりません！")
            print("    Steamから「ファイルの整合性を確認」を実行して環境を修復してください。")
            return False
    return True

def restore_vanilla(hoi4_path: Path, silent: bool = False):
    """バックアップからバニラを復元し、バックアップとステートを完全消去する"""
    target_dir = hoi4_path / "gfx" / "cursors"
    backup_dir = hoi4_path / "gfx" / BACKUP_DIR_NAME
    state_file = hoi4_path / "gfx" / STATE_FILE_NAME
    current_state = get_current_state(hoi4_path)
    
    if current_state == "VANILLA" and not backup_dir.exists():
        if not silent:
            print("[*] 既に完全にバニラ状態です。")
        return True
        
    if not backup_dir.exists():
        print("[!] エラー: 復元するためのバックアップが見つかりません。")
        return False
        
    if not silent:
        print("[*] バニラ環境に復元中...")
        
    # 1. 適用中のファイルを削除
    for item in target_dir.iterdir():
        if item.is_file() and item.suffix.lower() in ['.cur', '.ani']:
            try:
                item.unlink()
            except Exception:
                pass
            
    # 2. バックアップから復元
    for item in backup_dir.iterdir():
        if item.is_file() and item.suffix.lower() in ['.cur', '.ani']:
            shutil.copy2(item, target_dir)
            
    # 3. 痕跡を完全消去し、ステートを初期化
    try:
        shutil.rmtree(backup_dir)
        if state_file.exists():
            state_file.unlink()
        if not silent:
            print("[+] 完全なバニラ状態に復元し、バックアップ等の痕跡を消去しました！")
    except Exception as e:
        print(f"[!] 復元完了。一部消去に失敗しました: {e}")
        set_current_state(hoi4_path, "VANILLA")
        
    return True

def apply_cursors(hoi4_path: Path, faction: str):
    source_dir = CUSTOM_CURSORS_DIR / faction
    target_dir = hoi4_path / "gfx" / "cursors"
    current_state = get_current_state(hoi4_path)
    
    if not source_dir.exists():
        print(f"[!] エラー: {source_dir} が見つかりません。")
        return

    if current_state == faction:
        print(f"[*] 既に {faction} のカーソルが適用されています。")
        return

    # バックアップの安全確認と作成
    if not setup_backup(hoi4_path):
        return

    # 別の陣営が適用中なら、一度サイレントにバニラへ戻す
    if current_state != "VANILLA":
        print(f"[*] 現在 {current_state} が適用中です。競合を防ぐためバニラにリセットします...")
        restore_vanilla(hoi4_path, silent=True)
        # リセット後に改めてバニラのバックアップを作成
        setup_backup(hoi4_path)

    print(f"[*] {faction} のカスタムカーソルを適用中...")
    patched_count = 0
    for item in source_dir.iterdir():
        if item.is_file() and item.suffix.lower() in ['.cur', '.ani']:
            shutil.copy2(item, target_dir)
            patched_count += 1
            
    if patched_count > 0:
        set_current_state(hoi4_path, faction)
        print(f"[+] {faction} のカーソル適用が完了しました！（状態を {faction} として保存）")
    else:
        print("[!] 警告: .cur または .ani ファイルが見つかりませんでした。")

def main():
    print("="*60)
    print(" HoI4 mnds Cursor Changer (ver.alpha)")
    print("="*60)

    hoi4_path = get_default_hoi4_path()
    
    if not (hoi4_path and verify_hoi4_path(hoi4_path)):
        while True:
            manual_path = input("HoI4のインストール先フォルダのパスを入力してください:\n> ").strip('\'"')
            hoi4_path = Path(manual_path)
            if verify_hoi4_path(hoi4_path):
                break
            print("[!] 無効なパスです。")

    # 起動時に ASCII アートを表示
    mnds_ascii_art()

    while True:
        current_state = get_current_state(hoi4_path)
        print("\n" + "="*40)
        print(f" 現在の状態: 【 {current_state} 】")
        print("="*40)
        print("  [1] イタリアさんカーソル (SAV) を適用")
        print("  [2] 中国さんカーソル (CIN) を適用")
        print("  [3] フランスさんカーソル (FRC) を適用")
        print("  [4] 日本さんカーソル (GPN) を適用")
        print("  [5] イギリスさんカーソル (IGH) を適用")
        print("  [6] ドイツさんカーソル (PRS) を適用")
        print("  [7] ソ連さんカーソル (SOV) を適用")
        print("  [8] バニラ (VANILLA) に復元してクリーンアップ")
        print("  [0] 終了")
        
        choice = input("番号を入力 > ").strip()
        
        if choice == '1':
            apply_cursors(hoi4_path, "SAV")
        elif choice == '2':
            apply_cursors(hoi4_path, "CIN")
        elif choice == '3':
            apply_cursors(hoi4_path, "FRC")
        elif choice == '4':
            apply_cursors(hoi4_path, "GPN")
        elif choice == '5':
            apply_cursors(hoi4_path, "IGH")
        elif choice == '6':
            apply_cursors(hoi4_path, "PRS")
        elif choice == '7':
            apply_cursors(hoi4_path, "SOV")
        elif choice == '8':
            restore_vanilla(hoi4_path)
        elif choice == '0':
            print("終了します。")
            break
        else:
            print("[!] 無効な入力です。")

if __name__ == "__main__":
    main()