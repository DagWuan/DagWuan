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
username = input(f"{Colorate.Diagonal(Colors.blue_to_red, 'Nhập Username: ')}{reset}")
nd = input(f"{Colorate.Diagonal(Colors.blue_to_green, 'Nhập Nội Dung: ')}{reset}").replace(" ", " ")
so_lan = int(input(f"{Colorate.Diagonal(Colors.blue_to_purple, 'Nhập số lần gửi: ')}{reset}"))

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
