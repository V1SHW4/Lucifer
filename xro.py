try:
    import sys
    import requests
    from time import sleep
    import time
    from time import sleep
    import os
    os.system('clear')
except Exception as e:
    print(e)
    sys.exit()
def slow(M):
    for c in M + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(1. / 50)

print('\33[32m'"""██╗░░░░░██╗░░░██╗░█████╗░██╗███████╗███████╗██████╗░
██║░░░░░██║░░░██║██╔══██╗██║██╔════╝██╔════╝██╔══██╗
██║░░░░░██║░░░██║██║░░╚═╝██║█████╗░░█████╗░░██████╔╝
██║░░░░░██║░░░██║██║░░██╗██║██╔══╝░░██╔══╝░░██╔══██╗
███████╗╚██████╔╝╚█████╔╝██║██║░░░░░███████╗██║░░██║
╚══════╝░╚═════╝░░╚════╝░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝""")
print("""m.                                   ,_
         ' ;M;                                ,;m `
           ;M;.           ,      ,           ;SMM;
          ;;Mm;         ,;  ____  ;,         ;SMM;
         ;;;MM;        ; (.MMMMMM.) ;       ,SSMM;;
       ,;;;mMp'        l  ';mmmm;/  j       SSSMM;;
     .;;;;;MM;         .\,.mmSSSm,,/,      ,SSSMM;;;
    ;;;;;;mMM;        .;MMmSSSSSSSmMm;     ;MSSMM;;;;
   ;;;;;;mMSM;     ,_ ;MMmS;;;;;;mmmM;  -,;MMMMMMm;;;;
  ;;;;;;;MMSMM;     \"*;M;( ( '') );m;*"/ ;MMMMMM;;;;;,
 .;;;;;;mMMSMM;      \(@;! _     _ !;@)/ ;MMMMMMMM;;;;;,
 ;;;;;;;MMSSSM;       ;,;.*o*> <*o*.;m; ;MMMMMMMMM;;;;;;,
.;;;;;;;MMSSSMM;     ;Mm;           ;M;,MMMMMMMMMMm;;;;;;.
;;;;;;;mmMSSSMMMM,   ;Mm;,   '-    ,;M;MMMMMMMSMMMMm;;;;;;;
;;;;;;;MMMSSSMMMMMMMm;Mm;;,  ___  ,;SmM;MMMMMMSSMMMM;;;;;;;;
;;'";;;MMMSSSSMMMMMM;MMmS;;,  "  ,;SmMM;MMMMMMSSMMMM;;;;;;;;.
!   ;;;MMMSSSSSMMMMM;MMMmSS;;._.;;SSmMM;MMMMMMSSMMMM;;;;;;;;;
    ;;;;*MSSSSSSMMMP;Mm*"'q;'   `;p*"*M;MMMMMSSSSMMM;;;;;;;;;
    ';;;  ;SS*SSM*M;M;'     `-.        ;;MMMMSSSSSMM;;;;;;;;;,
     ;;;. ;P  `q; qMM.                 ';MMMMSSSSSMp' ';;;;;;;
     ;;;; ',    ; .mm!     \.   `.   /  ;MMM' `qSS'    ';;;;;;
     ';;;       ' mmS';     ;     ,  `. ;'M'   `S       ';;;;;
      `;;.        mS;;`;    ;     ;    ;M,!     '  luk   ';;;;
       ';;       .mS;;, ;   '.   ;   oMM;                ;;;;
        ';;      MMmS;; `,   ;._.' -_.'MM;                 ;;;
         `;;     MMmS;;; ;   ;      ;  MM;                 ;;;
           `'.   'MMmS;; `;) ',    .' ,M;'                 ;;;
              \    '' ''; ;   ;    ;  ;'                   ;;
               ;        ; `,  ;    ;  ;                   ;;
                        |. ;  ; (. ;  ;      _.-.         ;;
           .-----..__  /   ;  ;   ;' ;\  _.-" .- `.      ;;
         ;' ___      `*;   `; ';  ;  ; ;'  .-'    :      ; """)
print("'\33[31m'                TOOL BROUGHT BACK TO LIFE BY CEO xRO\nVERSION 1.1 by xRO")
rs = requests.session()
user = input(f"'\33[34m' Enter The Target >> ")
head = {
    'HOST': "www.instagram.com",
    'KeepAlive' : 'True',
    'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
    'Cookie': 'cookie',
    'Accept' : "*/*",
    'ContentType' : "application/x-www-form-urlencoded",
    "X-Requested-With" : "XMLHttpRequest",
    "X-IG-App-ID": "936619743392459",
    "X-Instagram-AJAX" : "missing",
    "X-CSRFToken" : "missing",
    "Accept-Language" : "en-US,en;q=0.9"
}
try:
    url = f'https://www.instagram.com/{user}/?__a=1'
    info = rs.get(url, headers=head).json()
except Exception:
    print(f"TOOL IS DOWN FOR SOME REASON,")
    sys.exit()


try:
    user = str(info['graphql']['user']['username'])
    ID = str(info['graphql']['user']['id'])
    private = str(info['graphql']['user']['is_private'])
    verified = str(info['graphql']['user']['is_verified'])
    business = str(info['graphql']['user']['is_business_account'])
    highlight = str(info['graphql']['user']['highlight_reel_count'])
    full_name = str(info['graphql']['user']['full_name'])
    posts = str(info['graphql']['user']['edge_owner_to_timeline_media']['count'])
    followers = str(info['graphql']['user']['edge_followed_by']['count'])
    following = str(info['graphql']['user']['edge_follow']['count'])
    link = str(info['graphql']['user']['external_url'])
    avatar = str(info['graphql']['user']['profile_pic_url_hd'])
    last = requests.get(avatar)
    last_avatar = last.headers['last-modified']
    bio = str(info['graphql']['user']['biography'])
except Exception:
    print(f"[-] Check The Target Pls..,")
    sys.exit()

slow(f"""
[>] Username : [ {user} ]
[>] ID : [ {ID} ]
[>] Full Name : [ {full_name} ]
[>] Private Account : [ {private} ]
[>] Verified : [ {verified} ]
[>] Business Account : [ {business} ]
[>] Number Of Highlight : [ {highlight} ]
[>] Number Of Posts : [ {posts} ]
[>] Followers : [ {followers} ]
[>] Following Them : [ {following} ]
[>] The Link : [ {link} ]
[>] Last Time Was Avatar Changed [ {last_avatar} ]
[>] Avatar Link : [ {avatar} ]
[>] Bio : \n{bio}
""")
print("THIS VERSION ALL COPYRIGHTS BY xRO.IF ANY ONE UPDATE THIS TOOL,ONLY THEN CAN CHANGE OWNER CREDITS")
