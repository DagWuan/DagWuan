import requests
import os
import sys
import datetime
import hashlib
import uuid
from colorama import Fore
import threading
import base64
import os
import time
import re
import json
import random
import requests
import socket
import sys
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# Kiểm tra và cài đặt thư viện cần thiết
try:
    from faker import Faker
    from requests import session
    from colorama import Fore, Style
    import pystyle
except ImportError:
    os.system("pip install faker requests colorama bs4 pystyle")
    os.system("pip3 install requests pysocks")
    print('__Vui Lòng Chạy Lại Tool__')
    sys.exit()

# Tạo hoặc đọc khóa mã hóa bằng base64
secret_key = base64.urlsafe_b64encode(os.urandom(32))

# Mã hóa và giải mã dữ liệu bằng base64
def encrypt_data(data):
    return base64.b64encode(data.encode()).decode()

def decrypt_data(encrypted_data):
    return base64.b64decode(encrypted_data.encode()).decode()

# Màu sắc cho hiển thị
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
end = '\033[0m'

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    banner = f"""
\033[1;33m██████╗░██╗░░░██╗████████╗░█████╗░░█████╗░██╗░░░░░
\033[1;35m██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
\033[1;36m██████╔╝╚██╗░██╔╝░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;37m██╔══██╗░╚████╔╝░░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;32m██║░░██║░░╚██╔╝░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗
\033[1;31m╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝\n
\033[1;97mTool By: \033[1;32mDUY KHÁNH            \033[1;97mPhiên Bản: \033[1;32mV4    
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m<>\033[1;97m]\033[1;95m BOX ZALO\033[1;31m : \033[1;36mhttps://zalo.me/g/nguadz335
\033[1;97m[\033[1;91m<>\033[1;97m]\033[1;93m YOUTUBE\033[1;31m : \033[1;32mREVIEWTOOL247NK
\033[1;97m[\033[1;91m<>\033[1;97m]\033[1;32m ADMIN\033[1;31m : \033[1;33mDUYKHANH
\033[97m════════════════════════════════════════════════  
"""
    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.000001)

def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_data = response.json()
        ip_address = ip_data['ip']
        return ip_address
    except Exception as e:
        print(f"Lỗi khi lấy địa chỉ IP: {e}")
        return None

def display_ip_address(ip_address):
    if ip_address:
        banner()
        print(f"\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mĐịa chỉ IP : {ip_address}")
    else:
        print("Không thể lấy địa chỉ IP của thiết bị.")

def luu_thong_tin_ip(ip, key, expiration_date):
    data = {ip: {'key': key, 'expiration_date': expiration_date.isoformat()}}
    encrypted_data = encrypt_data(json.dumps(data))

    with open('ip_key.json', 'w') as file:
        file.write(encrypted_data)

def tai_thong_tin_ip():
    try:
        with open('ip_key.json', 'r') as file:
            encrypted_data = file.read()
        data = json.loads(decrypt_data(encrypted_data))
        return data
    except FileNotFoundError:
        return None

def kiem_tra_ip(ip):
    data = tai_thong_tin_ip()
    if data and ip in data:
        expiration_date = datetime.fromisoformat(data[ip]['expiration_date'])
        if expiration_date > datetime.now():
            return data[ip]['key']
    return None

def generate_key_and_url(ip_address):
    ngay = int(datetime.now().day)
    key1 = str(ngay * 27 + 27)
    ip_numbers = ''.join(filter(str.isdigit, ip_address))
    key = f'NDK{key1}{ip_numbers}'
    expiration_date = datetime.now().replace(hour=23, minute=59, second=0, microsecond=0)
    url = f'https://bdquan.blogspot.com/2025/02/webkey.html?ma={key}'
    return url, key, expiration_date

def da_qua_gio_moi():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    return now >= midnight

def get_shortened_link_phu(url):
    """
    Hàm để rút gọn URL bằng một dịch vụ API.
    """
    try:
        token = "679e1efb13055f3d4e6e088f"  # Thay bằng API Token Của Bạn
        api_url = f"https://link4m.co/api={token}&url={url}"

        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"status": "error", "message": "Không thể kết nối đến dịch vụ rút gọn URL."}
    except Exception as e:
        return {"status": "error", "message": f"Lỗi khi rút gọn URL: {e}"}

def main():
    ip_address = get_ip_address()
    display_ip_address(ip_address)

    if ip_address:
        existing_key = kiem_tra_ip(ip_address)
        if existing_key:
            print(f"\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;35mTool còn hạn, mời bạn dùng tool...")
            time.sleep(2)
        else:
            if da_qua_gio_moi():
                print("\033[1;33mQuá giờ sử dụng tool !!!")
                return

            url, key, expiration_date = generate_key_and_url(ip_address)

            with ThreadPoolExecutor(max_workers=2) as executor:
                print("\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;32mNhập 1 Để Lấy Key \033[1;33m( Free )")

                while True:
                    try:
                        choice = input("\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;34mNhập lựa chọn: ")
                        print("\033[97m════════════════════════════════════════════════")
                        if choice == "1":
                            yeumoney_future = executor.submit(get_shortened_link_phu, url)
                            yeumoney_data = yeumoney_future.result()
                            if yeumoney_data and yeumoney_data.get('status') == "error":
                                print(yeumoney_data.get('message'))
                                return
                            else:
                                link_key_yeumoney = yeumoney_data.get('shortenedUrl')
                                print('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;35mLink Để Vượt Key Là \033[1;36m:', link_key_yeumoney)

                            while True:
                                keynhap = input('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;33mKey Đã Vượt Là: \033[1;32m')
                                if keynhap == key:
                                    print('Key Đúng Mời Bạn Dùng Tool')
                                    sleep(2)
                                    luu_thong_tin_ip(ip_address, keynhap, expiration_date)
                                    return
                                else:
                                    print('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;35mKey Sai Vui Lòng Vượt Lại Link \033[1;36m:', link_key_yeumoney)
                    except ValueError:
                        print("Vui lòng nhập số hợp lệ.")
                    except KeyboardInterrupt:
                        print("\n\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mCảm ơn bạn đã dùng Tool !!!")
                        sys.exit()

if __name__ == '__main__':
    main()

username = input(f"{Fore.YELLOW}Nhập Username: {Fore.RESET}")
nd = input(f"{Fore.CYAN}Nhập Nội Dung: {Fore.RESET}").replace(" ", " ")
so_lan = int(input(f"{Fore.GREEN}Nhập số lần gửi: {Fore.RESET}"))

url = "https://ngl.link/api/submit"
headers = {
    "accept": "*/*",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "user-agent": "Mozilla/5.0",
    "origin": "https://ngl.link",
    "referer": f"https://ngl.link/{username}"
}

for i in range(so_lan):
    data = {
        "username": username,
        "question": nd,
        "deviceId": str(uuid.uuid4()),
        "gameSlug": "",
        "referrer": ""
    }
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200 and "questionId" in response.json():
        print(f"{Fore.GREEN}Đã gửi {Fore.YELLOW}{i + 1} {Fore.CYAN}lần {Fore.MAGENTA}Nội Dung: '{nd}' {Fore.WHITE}Đến: '{username}' {Fore.GREEN}Trạng Thái: Thành Công {Fore.RESET}")
    elif "Could not find user" in response.text:
        print(f"{Fore.RED}Username Sai Hoặc Không Hợp Lệ!{Fore.RESET}")
        break
    else:
        print(f"{Fore.GREEN}Đã gửi {Fore.YELLOW}{i + 1} {Fore.CYAN}lần {Fore.MAGENTA}Nội Dung: '{nd}' {Fore.WHITE}Đến: '{username}' {Fore.GREEN}Trạng Thái: {Fore.RED} Thất Bại{Fore.RESET}")
