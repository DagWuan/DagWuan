import time
from datetime import datetime, timedelta
import sys
import os
import json
import requests
from pystyle import Colors, Colorate

# Các màu sắc
do = "\033[1;31m"
luc = "\033[1;32m"
xanhla = "\033[1;32m"
trang = "\033[1;37m"
ndp_tool = "\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"

# Xóa màn hình
os.system("cls" if os.name == "nt" else "clear")

# Hiển thị banner
def banner():
    os.system("cls" if os.name == "nt" else "clear")
    banner = f"""
                  {luc}© Bản Quyền BDQ09 ! Tool VIPBRO !!!
                    
           {do}   ██████╗ ██████╗  ██████╗  █████╗  █████╗  
             {trang} ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗ 
           {do}   ██████╦╝██║  ██║██║██╗██║██║  ██║╚██████║ 
             {trang} ██╔══██╗██║  ██║╚██████╔╝██║  ██║ ╚═══██║ 
           {do}   ██████╦╝██████╔╝ ╚═██╔═╝ ╚█████╔╝ █████╔╝ 
             {trang} ╚═════╝ ╚═════╝   ╚═╝     ╚════╝  ╚════╝  """
    print(banner)
    print(thanh)  # In thanh ra màn hình

# Hàm lấy địa chỉ IP và kiểm tra tình trạng sống
def get_ip_status():
    try:
        ip = requests.get('https://api.ipify.org').text  # Lấy địa chỉ IP công cộng
        response = requests.get(f'https://www.google.com', timeout=5)  # Kiểm tra kết nối internet
        if response.status_code == 200:
            return ip, f"{xanhla}live"
        else:
            return ip, f"{do}die"
    except requests.RequestException:
        return 'Không xác định', 'die'

# Hàm hiển thị thông tin key
def show_key_info(key):
    ip, status = get_ip_status()  # Lấy IP và trạng thái
    current_date = datetime.now().strftime("%d-%m-%Y")  # Lấy ngày hiện tại theo định dạng DD-MM-YYYY

    print(f"""{luc}
╔════════════════════════════════════╗
║           {trang}Thông Tin Tool{luc}           ║{trang}
╠════════════════════════════════════╣
║ {trang}=> Admin: Bùi Đăng Quân            ║
║ {trang}=> Ngày: {current_date}                ║
║ {trang}=> Địa Chỉ IP: {ip}      ║
║ {trang}=> Trạng Thái IP: [{status}{trang}]           ║ 
╚════════════════════════════════════╝
""")
    
    print(f"{do}Tool đang update dự kiến sẽ là {trang}ngày 1-4-2025")
    print(f"{do}Hãy lên YTb: {trang}DagWuan Share Tools để được cập nhật tools mới!!")
