import os
import shutil
import platform
from pathlib import Path

# --- 設定 ---
CUSTOM_CURSORS_DIR = Path("custom_cursors")
BACKUP_DIR_NAME = "cursors_backup"

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
    cursors_path = path / "gfx" / "cursors"
    return cursors_path.exists()

def setup_backup(hoi4_path: Path):
    cursors_dir = hoi4_path / "gfx" / "cursors"
    backup_dir = hoi4_path / "gfx" / BACKUP_DIR_NAME
    
    if not backup_dir.exists():
        print(f"[*] バニラファイルのバックアップを作成中: {backup_dir}")
        shutil.copytree(cursors_dir, backup_dir)
        print("[+] バックアップ完了。")
    else:
        print("[*] バックアップは既に存在します。")

def apply_cursors(hoi4_path: Path, faction: str):
    source_dir = CUSTOM_CURSORS_DIR / faction
    target_dir = hoi4_path / "gfx" / "cursors"
    backup_dir = hoi4_path / "gfx" / BACKUP_DIR_NAME
    
    if not source_dir.exists():
        print(f"[!] エラー: {source_dir} が見つかりません。")
        return

    # 【追記】別陣営のカーソルが混ざるのを防ぐため、適用前に必ずバックアップで上書きし、綺麗な状態にする
    if backup_dir.exists():
        print("[*] 適用前に現在の状態をクリーンアップ（リセット）しています...")
        for item in backup_dir.iterdir():
            if item.is_file() and item.suffix.lower() in ['.cur', '.ani']:
                shutil.copy2(item, target_dir)

    print(f"[*] {faction} のカーソルを適用中...")
    for item in source_dir.iterdir():
        if item.is_file() and item.suffix.lower() in ['.cur', '.ani']:
            shutil.copy2(item, target_dir)
            print(f"  -> {item.name} を上書きしました")
            
    print(f"[+] {faction} のカーソルの適用が完了しました！")


def restore_vanilla(hoi4_path: Path):
    target_dir = hoi4_path / "gfx" / "cursors"
    backup_dir = hoi4_path / "gfx" / BACKUP_DIR_NAME
    
    if not backup_dir.exists():
        print("[!] エラー: バックアップが見つかりません。すでにバニラ状態か、手動で削除されています。")
        return
        
    print("[*] バニラのカーソルを復元中...")
    
    # 1. 適用した .cur と .ani を削除
    for item in target_dir.iterdir():
        if item.is_file() and item.suffix.lower() in ['.cur', '.ani']:
            try:
                item.unlink()
            except Exception as e:
                print(f"[!] {item.name} の削除に失敗しました: {e}")
            
    # 2. バックアップから復元
    for item in backup_dir.iterdir():
        if item.is_file() and item.suffix.lower() in ['.cur', '.ani']:
            shutil.copy2(item, target_dir)
            
    # 3. 現状復帰のためのクリーンアップ（フォルダの完全削除）
    print("[*] 復元が完了しました。バックアップフォルダを削除してクリーンアップします...")
    try:
        shutil.rmtree(backup_dir)
        print("[+] 完全にバニラの状態に戻り、痕跡を消去しました！")
    except Exception as e:
        print(f"[!] 復元は完了しましたが、バックアップフォルダの削除に失敗しました: {e}")

def main():
    print("="*50)
    print(" HoI4 Custom Cursor Patcher (.cur & .ani 対応版)")
    print("="*50)
    
    hoi4_path = get_default_hoi4_path()
    print(f"[*] OS自動検知: {platform.system()}")
    
    if hoi4_path and verify_hoi4_path(hoi4_path):
        print(f"[+] HoI4ディレクトリを自動検出しました: {hoi4_path}")
    else:
        print("[-] デフォルトのパスにHoI4が見つかりませんでした。")
        while True:
            manual_path = input("HoI4のインストール先フォルダパスを入力してください:\n> ").strip()
            manual_path = manual_path.strip('\'"')
            hoi4_path = Path(manual_path)
            
            if verify_hoi4_path(hoi4_path):
                print("[+] パスを確認しました。")
                break
            else:
                print("[!] 無効なパスです。'gfx/cursors' フォルダが存在するディレクトリを指定してください。")

    print("\n" + "-"*30)
    setup_backup(hoi4_path)
    
    while True:
        print("\n" + "="*30)
        print("実行したい操作を選んでください:")
        print(" [1] イタリア(ITA) カーソルを適用")
        print(" [2] 日本(JPN) カーソルを適用")
        print(" [3] バニラ(Vanilla) カーソルを復元")
        print(" [0] 終了")
        print("="*30)
        
        choice = input("番号を入力 > ").strip()
        
        if choice == '1':
            apply_cursors(hoi4_path, "ITA")
        elif choice == '2':
            apply_cursors(hoi4_path, "JPN")
        elif choice == '3':
            restore_vanilla(hoi4_path)
        elif choice == '0':
            print("終了します。")
            break
        else:
            print("[!] 無効な入力です。")

if __name__ == "__main__":
    main()