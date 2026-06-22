import random
def mnds_ascii_art():
    aa1 = r"""
           ▲
          / \
         /   \
        /     \
       / PAX   \
      /  TIBIM  \
     /___________\
    |             |
    |  ┌-┐   ┌-┐  |
    |  |・|   |・|  |  ＜ フッ
    |  └-┘   └-┘  |
    |      v      |
     \    ―     /
      ／￣￣￣￣＼
    """
    #このAAはGemini作
    aa2 = r"""
           ▲
          / \
         /   \
        /     \
       / PAX   \
      /  TIBIM  \
     /___________\
    |             |
    |  ┌-┐   ┌-┐  |
    |  |○|   |○|  |  ＜ えっ！？
    |  └-┘   └-┘  |
    |      o      |
     \    △     /
      ／￣￣￣￣＼
    """
    #このAAはGemini作
    aa3 = r"""
                                                    -__//__`                                        
                                                  `enLeB":jA                                        
                                                 =N+  "2`  ^X{!`                                    
                                                "M`   ;T     :5R?                                   
                                               ,m/    `<.      ^BP'                                 
                                               o{`     t:       `uM!                                
                                              y6.     .Xi         =Nj                               
                                             =B"      ,,,'          Hf                              
                                            =M~   `*SYB&{LL|        .S^                             
                                           +k'^!?XrvXE"    "rS|"     ~$                             
                                          iMA?v'` ;f`         .1/S_   _#                            
                                        /wh"      "       ``     '=+=, H*                           
                                      /$<-   ``<<<?iiiv"=/*=        -A]'S                           
                                    <4=  ^!yv=_   HuuuP[."?/!/<!      _4S                           
                                  .)K"`-3u{.)=    < SB`=.'czL/|T3wu,.,. el                          
                                 _H"5a(^,v2+2"      SB   `z^ _AZ"i-^9vk `iA                         
                                "HYm!"l6'  #"Y+~` `;1?<~~"B*~+q"R|  @SY*k!gi'                       
                              !m4BZ!+iM2L: B)'v%@DDu++HGRNGB/HT!29+*M=  GviBj                       
                              ^@K*n===c@ARB@A4C*4.-j =   N5R2?lSH"!H!! "Y<l?4B"                     
                              t".4! _6sN9vYR"`'3! -z     & `?G"`-"*M4xANBB4@2GB                     
                              t:.wt[AA/ !+`=i` 1  A/ " !b`!!``*RB2e4!i5=m2u6f?B^                    
                             ,E;"?qR. =O; `.!G. ^|` =@(uxiiiR@RMRMhL/ =v,ti9GTB&"                   
                            rRBBn1{5`Tq,[--">5h/  r2+"Xuu"i"N''! *tQT  B f%-$5eXB:                  
                          `r$v^U| uHedB7GBH#KlB#J]_-`B    "!_?[=    R" &  H Je$Bm'                  
                          1S H! `1l|2H5i_<` "-Bv?^__"B/,  ^eeAAi!   @^ ` |] 1/ "o6%<"               
                          rOG  ?b" Q03!/  /++r^R" !  vw   ,<<<_   'R=^; "*` ,q^`  <fdB@f"           
                      -vh+r#/2$@@  QG     ^m##i/1     _iL?^  .!vvtQ"<fw=X"+6!|ir+!!  -v9B#5~        
                     "5, ;' +r'[M_ R$-   ^++, "/-         !+++,  +UB"   M! -4`   "=uv"_  =X@A_      
                    `B` !Me[!T; NNu-^"    `'|1*     ` *!w1"       3B'   5  ~A`     ^*Rl*:  `H@"     
                    !B ."#!!A*6'~H&Be*+++U=;     "!?o~!"`        *A!D  4_ "e:         =4*e   |di    
                     B       v(gmz~  `')Mu`                   "vNA`*6''c(uO|     !_`    =i*   ^&    
                    "B      wfr^    ?AR")[<!               ;km$wNR@BOG!^   o7      "=     , A4_w    
                  !&fB     ^"     !N! e, u9?VL(1,      .^fBgt+  ~u$B@v8B%,,]o,,,-   ^0U.    18BB    
                "6f. B          `{x_>Y|B%@i` [mBB#Kki*KRB7_`   ")' @[<hQU~~~~_?x)iKA,.B5.  "` _LK4~ 
               .5?   B^^*)+++=)z&U!_l!   3.  w .=////EB4`         /U  w`6!         :e[;B_  `@`  _OBe
               !B.  =B>_-.   -YHBmr-. "":sL/"R        6`        `*_   . `'           'Dq_   'w   `!M
               ,m+ v< /oSXaSX4o!'U+2SaM0z-!EB*        w       -t4^                   "_B5    /!    "
               _mN8wQ8=`      `1&3   ``.<1<^B!        w    `?E^`                     TMBy    :(     
            :<k&<.eo=           `)^        _"x=y+=c ^SR7!YTGB                      vAEo?a!!! .!`    
         .?XGJ  !p+              =1'iimBBBBBBBBSiiiX@&BR=   *_                 '!l4it"  -&BBY"B;    
       `JRC:   "N.  -/^         `HBB{m/l^!t{x!^^^^^^` B*                    :rAo3bL-     |K4nAB;    
     .vBA- )i  ,m"^CJ           v&r  JR:              "N,              !^/>$ZS4X|`    ~"fiXY`*H5    
    '%A-   Bi  ,ms,`            N!  'Uni           _- &BP               _)ybi",    :?i{4*!' 1H(@    
    XA`    d{ru$_              j@ ,{A_              XB&GBJ              |c@Q!:^"1>95Jh!`  !3e?lAnn/`
   mm.     i4N?`                NoQ)                XB+@lBf             "eu4uAS%u1'.  _eJfy?-  .Bmw0
   Bw     "P$_                  B0^                1B!B* !K6`           _v!!!,    "+*fXc!"   `*PTYL`
   /R4,  +Ni                    B3                .?B B*  ~6Q/            !i?9g2A6nSy*`   .!pT+(i!!Y
    `?&kOU"           ',        B3               "!wB/B*    "Ru`  *`       tX!m@>"    `+okAeYT"!5ATG
       fB!            B1        N(                 1B B*     .ANv.'G|`     +81*Bw^!/k@U94T5[ciGvA4e`
       ,B3           >B1        @                  _$|4*       ,l4f."A)=  "++6j<*SX3%|<?g*ft52mn_.  

    """
    #このAAはツールを使用


    # AAをリスト（配列）にまとめる
    aa_list = [aa1, aa2, aa3]
    
    # random.choice() を使ってリストの中からランダムに1つ選ぶ
    selected_aa = random.choice(aa_list)
    
    # 選ばれたAAを出力する
    print(selected_aa)

if __name__ == "__main__":
    mnds_ascii_art()