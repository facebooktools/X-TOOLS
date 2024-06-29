import requests,re,os,sys,random
from bs4 import BeautifulSoup as bs
from os import system as clr
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
def linex():
    print(f'──────────────────────────────────────────────')

def clear():
    clr('clear')
    #print(logo)

logo=("""\x1b[1;97m
::::    :::       ::::::::       :::::::::: 
:+:+:   :+:      :+:    :+:      :+:        
:+:+:+  +:+      +:+             +:+        
+#+ +:+ +#+      +#+             +#++:++#   
+#+  +#+#+#      +#+             +#+        
#+#   #+#+#      #+#    #+#      #+#        
###    ####       ########       ##########
──────────────────────────────────────────────
[®] 𝗔𝗨𝗧𝗛𝗢𝗥    : 𝗡𝗜𝗥𝗢𝗕 𝗫𝗗
[®] 𝗧𝗢𝗘𝗦 𝗧𝗬𝗣𝗘 : 𝗣𝗘𝗥𝗦𝗢𝗡𝗔𝗟
[®] 𝗦𝗨𝗕𝗝𝗘𝗖𝗧   : 𝗔𝗨𝗧𝗢 𝗙𝗥𝗜𝗘𝗡𝗗 𝗥𝗘𝗤𝗨𝗘𝗦𝗧 𝗦𝗘𝗡𝗗𝗥𝗘\x1b[1;97m
──────────────────────────────────────────────
""")

headers = {
        'authority': 'mbasic.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9,id;q=0.8,bn;q=0.7','cache-control': 'max-age=0','dpr': '1','referer': 'https://mbasic.facebook.com/photo/?fbid=302777205596562&set=a.178678128006471','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-full-version-list': '"Not/A)Brand";v="99.0.0.0", "Google Chrome";v="115.0.5790.171", "Chromium";v="115.0.5790.171"','sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"15.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.151 Safari/537.36','viewport-width': '534',
    }

recac=[]
def main():
    print(logo)
    req_acpt()

lop=0


def send():
    clear()
    try:
        ids_coki=('/sdcard/coki.txt')
        cokie=requests.get('https://raw.githubusercontent.com/facebooktools/X-TOOLS/main/coki.txt').text.splitlines()
    except:
        print(f'File Not founded')
        req_acpt()
    try:
        print(logo)
        ter_ids=input('[?] 𝗜𝗡𝗣𝗨𝗧 𝗧𝗔𝗥𝗚𝗘𝗧 𝗨𝗜𝗗  : ')
        ids =(ter_ids).splitlines()
    except:
        print(f'Uid Not founded')
        req_acpt()
    linex()
    clear()
    print(logo)
    for coke in cokie:
        for uid in ids:
            with ThreadPool(max_workers=100) as mylove:
                mylove.submit(req,coke,uid)
def req_acpt():
    clear()
    sec=send()
        



session=requests.Session()
sdrq=[]
def req(coke,uid):
    global lop
    url = f'https://mbasic.facebook.com/profile.php?id={uid}'
    r = bs(session.get(url,headers=headers,cookies={'Cookie': coke}).text, 'html.parser')
    follow_link = r.find('a', string='Add friend')
    if follow_link:
        follow_url = 'https://mbasic.facebook.com' + follow_link['href']
        if '/a/friends/profile/add/?subject_id=' in follow_url:
            session.get(follow_url,headers=headers,cookies={'Cookie': coke})
            sdrq.append(uid)
            print(f"[{len(sdrq)}] {G}𝗦𝗘𝗡𝗗 𝗗𝗢𝗡𝗘 : {A}{uid}|{r.find('title').text}")
    else:
        pass
        print(f"[😞] {R}𝗦𝗘𝗡𝗗𝗜𝗡𝗚 𝗘𝗥𝗢𝗥 {uid}")
    lop+=1                

main()