import time
from datetime import datetime, timedelta
import sys
import os
from pystyle import Colors, Colorate
import webbrowser
import requests

# Các màu sắc
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

# Đánh dấu bản quyền
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
        time.sleep(0.00125)

# Kiểm tra tính hợp lệ của key
def check_key_validity(key):
    # Giả sử bạn có danh sách các khóa hợp lệ
    valid_keys = ["KEY123", "KEY456", "VIPTOOL2025"]
    return key in valid_keys

remaining_time = None  # Đặt giá trị mặc định cho remaining_time
def enter_key():
    global remaining_time  # Sử dụng biến toàn cục remaining_time
    while True:
        key = input(f"\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập Key Để Sử Dụng Tool: \033[1;33m")
        
        # Kiểm tra tính hợp lệ của key
        if check_key_validity(key):
            print(f"\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mKey hợp lệ! \033[1;37mBạn có thể tiếp tục sử dụng tool.")
            
            # Tính thời gian hết hạn key (ví dụ: key có hiệu lực trong 24 giờ)
            expiration_time = (datetime.now() + timedelta(days=1))
            remaining_time = expiration_time - datetime.now()  # Tính thời gian còn lại

            # Ẩn key
            print(f"\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;35mThời gian còn lại của Key: \033[1;32m{remaining_time}")
            break
        else:
            print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;31mKey không hợp lệ! Vui lòng nhập lại.")

# Hiển thị lựa chọn tool
def show_tool_options():
    print (Colorate.Diagonal(Colors.blue_to_red, "────────────────────────────────────────────────────────────"))
    print (Colorate.Diagonal(Colors.blue_to_purple, "╔═════════════════════╗"))
    print (Colorate.Diagonal(Colors.blue_to_purple, "║  Các Loại Tool      ║"))
    print (Colorate.Diagonal(Colors.blue_to_purple, "╚═════════════════════╝"))

    print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m1\033[1;31m] \033[1;32mTools Gộp New \033[1;33m[\033[1;31mV1\033[1;33m] ")
    print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m2\033[1;31m] \033[1;32mTDS Facebook Vip\033[1;33m[\033[1;31mV2\033[1;33m] ")

    print (Colorate.Diagonal(Colors.blue_to_red, "────────────────────────────────────────────────────────────"))

# Hàm tải và thực thi mã từ URL
def execute_remote_script(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Kiểm tra mã lỗi HTTP
        exec(response.text)  # Thực thi mã Python từ URL
    except requests.exceptions.RequestException as e:
        print(f"\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;31mLỗi khi tải mã từ URL: {e}")
        sys.exit(1)

# Main function để điều hướng chương trình
def main():
    os.system("cls" if os.name == "nt" else "clear")
    banner()  # Hiển thị banner
    enter_key()  # Nhập key và kiểm tra
    show_tool_options()  # Hiển thị các lựa chọn tool

    while True:
        chon = str(input('\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;37m: \033[1;33m'))
        
        if chon == '1':
            execute_remote_script('https://raw.githubusercontent.com/DagWuan/DagWuan/refs/heads/main/Tool1.py')
            break
        elif chon == '2':
            execute_remote_script('https://raw.githubusercontent.com/DagWuan/DagWuan/refs/heads/main/tdsv.py')
            break
        else:
            print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;31mLựa chọn không hợp lệ, vui lòng nhập lại số 1 hoặc 2.\033[1;37m")

if __name__ == "__main__":
    main()
