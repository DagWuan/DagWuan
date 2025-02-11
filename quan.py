import time
from time import strftime
import os
import sys
import requests
import json
from time import sleep
from datetime import datetime, timedelta
import base64
import requests
import os
import subprocess
from pystyle import Colors, Colorate
from rich.console import Console
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
# màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
tim = '\033[1;39m'
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb = "\033[1;37m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'
os.system("cls" if os.name == "nt" else "clear")

# đánh dấu bản quyền
ndp_tool = "\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"

def banner():
    banner = f"""
\033[1;33m██████╗░░█████╗░░██████╗░░██╗░░░░░░░██╗██╗░░░██╗░█████╗░███╗░░██╗
\033[1;33m██╔══██╗██╔══██╗██╔════╝░░██║░░██╗░░██║██║░░░██║██╔══██╗████╗░██║
\033[1;33m██║░░██║███████║██║░░██╗░░╚██╗████╗██╔╝██║░░░██║███████║██╔██╗██║
\033[1;33m██║░░██║██╔══██║██║░░╚██╗░░████╔═████║░██║░░░██║██╔══██║██║╚████║
\033[1;33m██████╔╝██║░░██║╚██████╔╝░░╚██╔╝░╚██╔╝░╚██████╔╝██║░░██║██║░╚███║
\033[1;33m╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝
\033[1;31mTool By: Đăng Quân            \033[1;97mPhiên Bản: \033[1;32mV0.1       
\033[1;35mSource CodeBy: Duy Khánh       \033[1;31mRemaker: Đăng Quân
\033[97m───────────────────────────────────────────────────────────
\033[1;97m[\033[1;91m<>\033[1;97m]\033[1;95m Facebook\033[1;31m : \033[1;36mhttps://www.facebook.com/DagWuan185
\033[1;97m[\033[1;91m<>\033[1;97m]\033[1;93m YOUTUBE\033[1;31m : \033[1;32mDagWuan Share Tools
\033[1;97m[\033[1;91m<>\033[1;97m]\033[1;32m ADMIN\033[1;31m : \033[1;33mĐăng Quân
\033[97m────────────────────────────────────────────────────────────
"""

    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.00125)

os.system("cls" if os.name == "nt" else "clear")
banner()
print (Colorate.Diagonal(Colors.blue_to_red, "────────────────────────────────────────────────────────────"))
print (Colorate.Diagonal(Colors.blue_to_purple, "╔═════════════════════╗"))
print (Colorate.Diagonal(Colors.blue_to_purple, "║  Tool Trao Đổi Sub  ║"))
print (Colorate.Diagonal(Colors.blue_to_purple, "╚═════════════════════╝"))

print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m1.1\033[1;31m] \033[1;32mTDS TIKTOK \033[1;33m[\033[1;31mV1\033[1;33m] ")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m1.2\033[1;31m] \033[1;32mTDS TIKTOK \033[1;33m[\033[1;31mV2\033[1;33m] ")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m1.3\033[1;31m] \033[1;32mTDS TIKTOK & TIKTOK NOW")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m1.4\033[1;31m] \033[1;32mTDS INSTAGRAM")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m1.5\033[1;31m] \033[1;32mTOOL ĐỔI MK TĐS")

print (Colorate.Diagonal(Colors.blue_to_red, "────────────────────────────────────────────────────────────"))
print (Colorate.Diagonal(Colors.blue_to_purple, "╔═════════════════════╗"))
print (Colorate.Diagonal(Colors.blue_to_purple, "║  Tool Spam Sms      ║"))
print (Colorate.Diagonal(Colors.blue_to_purple, "╚═════════════════════╝"))
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m2.1\033[1;31m] \033[1;32mTOOL SPAM SMS \033[1;33m[\033[1;31mV1\033[1;33m] ")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m2.2\033[1;31m] \033[1;32mTOOL SPAM SMS \033[1;33m[\033[1;31mV2\033[1;33m] ")

print (Colorate.Diagonal(Colors.blue_to_red, "────────────────────────────────────────────────────────────"))
print (Colorate.Diagonal(Colors.blue_to_purple, "╔═════════════════════╗"))
print (Colorate.Diagonal(Colors.blue_to_purple, "║  Tool Đào Mail      ║"))
print (Colorate.Diagonal(Colors.blue_to_purple, "╚═════════════════════╝"))
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m3.1\033[1;31m] \033[1;32mTOOL ĐÀO MAIL")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m3.2\033[1;31m] \033[1;32mTOOL ĐÀO MAIL FULL MAIL")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m3.3\033[1;31m] \033[1;32mTOOL CHECK LIVE\DIE")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m3.4\033[1;31m] \033[1;32mTOOL CHECK VALID")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m3.5\033[1;31m] \033[1;32mTOOL REG ACC GARENA")

print (Colorate.Diagonal(Colors.blue_to_red, "────────────────────────────────────────────────────────────"))
print (Colorate.Diagonal(Colors.blue_to_purple, "╔═════════════════════════╗"))
print (Colorate.Diagonal(Colors.blue_to_purple, "║Tool Đào & Check Proxies ║"))
print (Colorate.Diagonal(Colors.blue_to_purple, "╚═════════════════════════╝"))
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m4.1\033[1;31m] \033[1;32mTOOL CHECK LIVE\DIE \033[1;33m[\033[1;31mV1\033[1;33m] ")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m4.2\033[1;31m] \033[1;32mTOOL CHECK LIVE\DIE \033[1;33m[\033[1;31mV2\033[1;33m] ")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m4.3\033[1;31m] \033[1;32mTOOL CHECK LIVE\DIE \033[1;33m[\033[1;31mV3 VIP\033[1;33m] ")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m4.4\033[1;31m] \033[1;32mTOOL ĐÀO PROXY \033[1;33m[\033[1;31mV1\033[1;33m] ")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m4.5\033[1;31m] \033[1;32mTOOL ĐÀO PROXY \033[1;33m[\033[1;31mV2\033[1;33m] ")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m4.6\033[1;31m] \033[1;32mTOOL ĐÀO PROXY \033[1;33m[\033[1;31mV3\033[1;33m] ")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m4.7\033[1;31m] \033[1;32mTOOL ĐÀO PROXY \033[1;33m[\033[1;31mV4\033[1;33m] ")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m4.8\033[1;31m] \033[1;32mTOOL ĐÀO PROXY \033[1;33m[\033[1;31mV5 VIP\033[1;33m] ")

print (Colorate.Diagonal(Colors.blue_to_red, "────────────────────────────────────────────────────────────"))
print (Colorate.Diagonal(Colors.blue_to_purple, "╔═════════════════════════╗"))
print (Colorate.Diagonal(Colors.blue_to_purple, "║Tool Encode & Dec        ║"))
print (Colorate.Diagonal(Colors.blue_to_purple, "╚═════════════════════════╝"))
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m5.1\033[1;31m] \033[1;32mTOOL DEC Hyperion_Deobf")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m5.2\033[1;31m] \033[1;32mTOOL DEC Kramer-Specter_Deobf")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m5.3\033[1;31m] \033[1;32mTOOL dump_marshal")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m5.4\033[1;31m] \033[1;32mTOOL Convert_Marshal-PYC")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m5.5\033[1;31m] \033[1;32mTOOL ENCODE MZB")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m5.6\033[1;31m] \033[1;32mTOOL ENCODE EMOJI")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m5.7\033[1;31m] \033[1;32mTOOL ENCODE EJULY-DUYKHANH")

print (Colorate.Diagonal(Colors.blue_to_red, "────────────────────────────────────────────────────────────"))
print (Colorate.Diagonal(Colors.blue_to_purple, "╔═════════════════════════╗"))
print (Colorate.Diagonal(Colors.blue_to_purple, "║Tool Aotu Golike         ║"))
print (Colorate.Diagonal(Colors.blue_to_purple, "╚═════════════════════════╝"))
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m6.1\033[1;31m] \033[1;32mTool Auto TikTok")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m6.2\033[1;31m] \033[1;32mTool Auto Instagram ")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m6.3\033[1;31m] \033[1;32mTool Auto Twitter")

print (Colorate.Diagonal(Colors.blue_to_red, "────────────────────────────────────────────────────────────"))
print (Colorate.Diagonal(Colors.blue_to_purple, "╔═════════════════════════╗"))
print (Colorate.Diagonal(Colors.blue_to_purple, "║Tool Của Các Idol Khác   ║"))
print (Colorate.Diagonal(Colors.blue_to_purple, "╚═════════════════════════╝"))
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m7.1\033[1;31m] \033[1;32mTOOL VLONG ZZ")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m7.2\033[1;31m] \033[1;32mTOOL TRỊNH HƯỚNG")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m7.3\033[1;31m] \033[1;32mTOOL MEOWMEOW")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m7.4\033[1;31m] \033[1;32mTOOL HDT-TOOL")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m7.5\033[1;31m] \033[1;32mTOOL LKZ TOOL")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m7.6\033[1;31m] \033[1;32mTOOL JIRAY TOOL")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m7.7\033[1;31m] \033[1;32mTOOL BETA TOOL")

print (Colorate.Diagonal(Colors.blue_to_red, "────────────────────────────────────────────────────────────"))
print (Colorate.Diagonal(Colors.blue_to_purple, "╔════════════════╗"))
print (Colorate.Diagonal(Colors.blue_to_purple, "║Tool Tiện ích   ║"))
print (Colorate.Diagonal(Colors.blue_to_purple, "╚════════════════╝"))
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m8.1\033[1;31m] \033[1;32mTOOL DOSS WEB VIP")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m8.2\033[1;31m] \033[1;32mTOOL REG PAGR PRO5")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m8.3\033[1;31m] \033[1;32mTool Rút Gọn Link ")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m8.4\033[1;31m] \033[1;32mGet Phản Hồi Từ Link")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m8.5\033[1;31m] \033[1;32mLọc Link Từ File")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m8.6\033[1;31m] \033[1;32mTOOL REG ACC FACEBOOK")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m8.7\033[1;31m] \033[1;32mTOOL SPAM NGL")

print (Colorate.Diagonal(Colors.blue_to_red, "────────────────────────────────────────────────────────────"))
print (Colorate.Diagonal(Colors.blue_to_purple, "╔════════════════╗"))
print (Colorate.Diagonal(Colors.blue_to_purple, "║Tool New Update ║"))
print (Colorate.Diagonal(Colors.blue_to_purple, "╚════════════════╝"))
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m9.1\033[1;31m] \033[1;32mTool máy tính")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m00\033[1;31m] \033[1;32mTHOÁT TOOL")

print (Colorate.Diagonal(Colors.blue_to_red, "────────────────────────────────────────────────────────────"))

chon = str(input('\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;37m: \033[1;33m'))


if chon == '00' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/thoattool/main/.github/workflows/main.yml').text)
    #tool tđs
if chon == '1.1' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/TDS-TIKTOK-V1/main/tool.py').text)
if chon == '1.2':
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Tdstikv2/main/00.py').text)
if chon == '1.3' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Tik-tiknow/main/1.py').text) 
if chon == '1.4' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/TDS-IG/main/3.py').text) 
elif chon == '1.5' : 
 exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Mktds/main/4.py').text) 
 #tool spam sms
if chon == '2.1' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Spamsmsv1/main/sms.py').text)
if chon == '2.2' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Spamsmsv2/main/smsv2.py').text)
    #tool đào mail
elif chon == '3.1' :
 exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Daomail/main/8.py').text)
elif chon == '3.2' :
 exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Full-mail/main/vietcode_toolmeow.py').text)
if chon == '3.3' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Checklivedie/main/p.py').text)
if chon == '3.4' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/checkvali/main/10.py').text)
if chon == '3.5' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Reggrn/main/Reggrn').text)
    #tool đào&check proxy
if chon == '4.1' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Checklivedieproxy/main/p.py').text)
if chon == '4.2' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Check-live-die-v2/main/q.py').text)
if chon == '4.3' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Checklivediev2/main/p.py').text)
if chon == '4.4' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Daoprxv1/main/daoprxv1.py').text)
if chon == '4.5' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Daoprxv2/main/p.py').text)
if chon == '4.6' :
  exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Daoproxyv3/main/p.py').text)
if chon == '4.7' :   
   exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Daoproxyv4/main/p.py').text)
if chon == '4.8' :  
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Daoproxyv4vip/main/p.py').text)
    #tool en&dec
if chon == '5.1' :
    exec(requests.get('https://raw.githubusercontent.com/KhanhNguyen9872/hyperion_deobfuscate/main/hyperion_deobf.py').text)
if chon == '5.2' :
     exec(requests.get('https://raw.githubusercontent.com/KhanhNguyen9872/kramer-specter_deobf/main/kramer-specter-deobf.py').text)
if chon == '5.3' :
    exec(requests.get('https://raw.githubusercontent.com/KhanhNguyen9872/dump_marshal_py/main/dump_marshal.py').text)
if chon == '5.4' :
    exec(requests.get('https://raw.githubusercontent.com/KhanhNguyen9872/Convert_Marshal-PYC/main/cv_marshal_pyc.py').text)
if chon == '5.5' :
	exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Encode-MZB/main/en.py').text)
if chon == '5.6' :
  exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Encode-Emoji-/main/p.py').text)
if chon == '5.7' :   
   exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Encode-ejuly-DUYKHANH/main/encode.py').text)
   #tool golike
if chon == '6.1' :  
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Golike/main/golike.py').text)
if chon == '6.2' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Golike-ig/main/p.py').text)
if chon == '6.3' :
     exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Golike-Twitter-/main/p.py').text)
     #tool idol khác 
if chon == '7.1' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Tool-vlong/main/p.py').text)
if chon == '7.2' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Tool-trinh-huong/main/huong.py').text)
if chon == '7.3' :
	exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Full-mail/main/vietcode_toolmeow.py').text)
if chon == '7.4' :
  exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Tool-hdt/main/p.py').text)
if chon == '7.5' :   
   exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Tool-lkz/main/p.py').text)
if chon == '7.6' :  
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Tool-jray/main/haha.py').text)
if chon == '7.7' :  
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Beta-tool/main/beta.py').text)
    #tool tiện ích
if chon == '8.1' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/DOSS-WEB/main/dos.py').text)
if chon == '8.2' :
     exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Reg-pro5-vip/main/reg.py').text)
if chon == '8.3' :
    exec(requests.get('https://raw.githubusercontent.com/DagWuan/DagWuan/refs/heads/main/Tools1.py').text)
if chon == '8.4' :
    exec(requests.get('https://raw.githubusercontent.com/DagWuan/DagWuan/refs/heads/main/Phanhoi.py').text)
if chon == '8.5' :
	exec(requests.get('https://raw.githubusercontent.com/DagWuan/DagWuan/refs/heads/main/Tools2.py').text)
if chon == '8.6' :
  exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Reg-fb/main/10.py').text)
if chon == '8.7' :
  exec(requests.get('https://raw.githubusercontent.com/DagWuan/DagWuan/refs/heads/main/SpamNGL.py').text)
  #tool tiện ích 
if chon == '9.1' :   
   exec(requests.get('https://raw.githubusercontent.com/Khanh23047/May-tinh/main/0.py').text)
else :
     exit()
