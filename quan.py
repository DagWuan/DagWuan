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
                  {luc}© Bản Quyền BDQ09 ! Tool VIPBRO !!!
                    
           {red}   ██████╗ ██████╗  ██████╗  █████╗  █████╗  
             {trang} ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗ 
           {red}   ██████╦╝██║  ██║██║██╗██║██║  ██║╚██████║ 
             {trang} ██╔══██╗██║  ██║╚██████╔╝██║  ██║ ╚═══██║ 
           {red}   ██████╦╝██████╔╝ ╚═██╔═╝ ╚█████╔╝ █████╔╝ 
             {trang} ╚═════╝ ╚═════╝   ╚═╝     ╚════╝  ╚════╝  
"""

    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.00125)

os.system("cls" if os.name == "nt" else "clear")
banner()
print (Colorate.Diagonal(Colors.blue_to_red, "────────────────────────────────────────────────────────────"))
print (Colorate.Diagonal(Colors.blue_to_purple, "╔═════════════════════╗"))
print (Colorate.Diagonal(Colors.blue_to_purple, "║  Các Loại Tool      ║"))
print (Colorate.Diagonal(Colors.blue_to_purple, "╚═════════════════════╝"))

print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m1\033[1;31m] \033[1;32mTools Gộp New \033[1;33m[\033[1;31mV1\033[1;33m] ")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m2\033[1;31m] \033[1;32mTDS Facebook Vip\033[1;33m[\033[1;31mV2\033[1;33m] ")

print (Colorate.Diagonal(Colors.blue_to_red, "────────────────────────────────────────────────────────────"))

# Sử dụng vòng lặp while để yêu cầu nhập lại khi sai
while True:
    chon = str(input('\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;37m: \033[1;33m'))
    
    if chon == '1':
        exec(requests.get('https://raw.githubusercontent.com/DagWuan/DagWuan/refs/heads/main/Tool1.py').text)
        break
    elif chon == '2':
        exec(requests.get('https://raw.githubusercontent.com/DagWuan/DagWuan/refs/heads/main/tdsv.py').text)
        break
    else:
        print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;31mLựa chọn không hợp lệ, vui lòng nhập lại số 1 hoặc 2.\033[1;37m")
