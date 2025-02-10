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
import requests
import os
import sys
import time
import psutil
import platform
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from bs4 import BeautifulSoup
import json
import requests
import time
from time import strftime
import os
import requests
import urllib.parse
from time import strftime
import os
from datetime import datetime
from time import sleep, strftime
import datetime
import uuid
import json
import sys
import random
import string
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import threading
from colorama import init, Fore  # Đảm bảo rằng thư viện colorama được import đúng cách

# Định nghĩa các màu
trang = Fore.WHITE
xanh_la = Fore.GREEN
xanh_duong = Fore.BLUE
do = Fore.RED
vang = Fore.YELLOW
tim = Fore.MAGENTA
xanhnhat = Fore.CYAN
reset = Fore.RESET
purple = "\033[1;35m"
bold = "\033[1m"
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
cyan = "\033[96m"

# Đánh dấu bản quyền
HĐ_tool = trang + trang + "[ " + do + "Bản quyền" + trang + " ] => "
mquang = trang + trang + "[ " + do + "Quảng cáo" + trang + " ] => "
thanh = trang + trang + '-------------------------------------------------------------------------'

# Hàm xóa màn hình
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Lấy ngày giờ hiện tại
def get_current_datetime():
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    return date, time

# Lấy địa chỉ IP công cộng
def get_ip_address():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        ip_info = response.json()
        return ip_info['ip']
    except requests.exceptions.RequestException as e:
        print("Error fetching IP address:", e)
        return None

# Lấy thông tin vị trí từ IP
def get_location(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        location_info = response.json()
        return location_info
    except requests.exceptions.RequestException as e:
        print("Error fetching location:", e)
        return None
        
# Hàm lấy thông tin hệ điều hành
def get_device_os():
    system_info = os.uname() if os.name != 'nt' else platform.system()
    if "Darwin" in system_info:
        return "iOS / Darwin"
    elif "Linux" in system_info:
        return "Android / Linux"
    else:
        return platform.system()

# Lấy thông tin RAM (đã sử dụng và còn lại)
def get_ram_info():
    memory_info = psutil.virtual_memory()
    total_ram = memory_info.total / (1024 ** 3)  # RAM tổng cộng (GB)
    available_ram = memory_info.available / (1024 ** 3)  # RAM còn lại (GB)
    used_ram = memory_info.used / (1024 ** 3)  # RAM đã sử dụng (GB)
    return f"{used_ram:.2f} GB / {total_ram:.2f} GB"

# Lấy thời tiết từ OpenWeatherMap
def get_weather(city_name, api_key):
    try: 
        weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
        response = requests.get(weather_url)
        if response.status_code == 200:
            weather_data = response.json()
            temperature = weather_data['main']['temp']
            weather_description = weather_data['weather'][0]['description']
            return f"{temperature}°C, {weather_description}"
        else:
            return "Không thể lấy thông tin thời tiết."
    except requests.exceptions.RequestException as e:
        return "Lỗi khi kết nối tới API thời tiết."

# Function to display banner with dynamic data
def display_banner():
    # Lấy ngày giờ, IP, vị trí và thời tiết
    current_date, current_time = get_current_datetime()
    ip_address = get_ip_address()
    if ip_address:
        location_info = get_location(ip_address)
        if location_info:
            city = location_info.get("city", "Không xác định")
            region = location_info.get("region", "Không xác định")
            country = location_info.get("country", "Không xác định")
            location = f"{city}, {region}, {country}"
        else:
            location = "Không thể lấy vị trí"
    else:
        location = "Không thể lấy địa chỉ IP"
    
    # Thêm thông tin thời tiết vào banner
    API_KEY = '9b9ca15d36dae89c5467c1812dd6aaec'  # Thay thế bằng API Key của bạn
    weather_info = get_weather(city, API_KEY)

    # Lấy thông tin hệ điều hành và RAM
    device_os = get_device_os()
    ram_info = get_ram_info()

    # Banner với thông tin động
    banner = f"""
    
██████╗░░█████╗░░██████╗░░██╗░░░░░░░██╗██╗░░░██╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██╔════╝░░██║░░██╗░░██║██║░░░██║██╔══██╗████╗░██║
██║░░██║███████║██║░░██╗░░╚██╗████╗██╔╝██║░░░██║███████║██╔██╗██║
██║░░██║██╔══██║██║░░╚██╗░░████╔═████║░██║░░░██║██╔══██║██║╚████║
██████╔╝██║░░██║╚██████╔╝░░╚██╔╝░╚██╔╝░╚██████╔╝██║░░██║██║░╚███║
╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝

    Ａｕｔｈｏｒ: DagWuan
    ＴｉｋＴｏｋ: b.lqbl0
    Ｆａｃｅｂｏｏｋ: https://www.facebook.com/DagWuan185

    ---------------------------
    Ngày:{reset} {current_date}
    Giờ:{reset} {current_time}
    Địa chỉ IP:{reset} {ip_address}
    Vị trí:{reset} {location}
    Thời tiết:{reset} {weather_info}
    Hệ điều hành:{reset} {device_os}
    RAM:{reset} {ram_info} 
    ---------------------------
    
                    ENTER ĐỂ VÀO TOOL SPAM SMS
    """
    
    # Hiển thị banner
    Anime.Fade(Center.Center(banner), Colors.purple_to_red, Colorate.Vertical, enter=True)

# Hàm chính
def main():
    clear_screen()
    display_banner()

if __name__ == "__main__":
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
