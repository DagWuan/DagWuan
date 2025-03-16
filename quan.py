import time
from datetime import datetime, timedelta
import sys
import os
import json
import requests
from pystyle import Colors, Colorate

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

KEY_FILE = "key_data.json"

# Xóa màn hình
os.system("cls" if os.name == "nt" else "clear")

# Hiển thị banner
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

# Lưu key vào file
def save_key(key, expiration):
    data = {"key": key, "expiration": expiration.isoformat()}
    with open(KEY_FILE, "w") as file:
        json.dump(data, file)

# Tải key từ file
def load_key():
    if os.path.exists(KEY_FILE):
        try:
            with open(KEY_FILE, "r") as file:
                data = json.load(file)
                expiration = datetime.fromisoformat(data["expiration"])
                if expiration > datetime.now():
                    return data["key"], expiration
        except:
            pass
    return None, None

# Kiểm tra key đã lưu
def check_saved_key():
    key, expiration = load_key()
    if key:
        time_left_seconds = (expiration - datetime.now()).total_seconds()
        hours = int(time_left_seconds // 3600)
        minutes = int((time_left_seconds % 3600) // 60)

        print(f"""{luc}
╔════════════════════════════════════╗
║       {trang}Thông Tin Key{luc}        ║
╠════════════════════════════════════╣
║ {trang}=> Key Tool: {key[:4]}***********{key[13:]}{luc}  ║
║ {trang}=> Thời Gian Còn Lại: {hours} Giờ {minutes} Phút{luc}  ║
║ {trang}=> Trạng Thái Key: Đang Hoạt Động{luc}  ║
╚════════════════════════════════════╝
""")
        return True
    return False

# Hiển thị menu chọn tool
def show_tool_options():
    print(Colorate.Diagonal(Colors.blue_to_red, "────────────────────────────────────────────────────────────"))
    print(Colorate.Diagonal(Colors.blue_to_purple, "╔═════════════════════╗"))
    print(Colorate.Diagonal(Colors.blue_to_purple, "║  Các Loại Tool      ║"))
    print(Colorate.Diagonal(Colors.blue_to_purple, "╚═════════════════════╝"))

    print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m1\033[1;31m] \033[1;32mTools Gộp New \033[1;33m[\033[1;31mV1\033[1;33m] ")
    print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m2\033[1;31m] \033[1;32mTDS Facebook Vip\033[1;33m[\033[1;31mV2\033[1;33m] ")

    print(Colorate.Diagonal(Colors.blue_to_red, "────────────────────────────────────────────────────────────"))

# Tải và thực thi mã từ URL
def execute_remote_script(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        exec(response.text)
    except requests.exceptions.RequestException as e:
        print(f"\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;31mLỗi khi tải mã từ URL: {e}")
        sys.exit(1)

# Yêu cầu nhập key mới nếu cần
def enter_key():
    while True:
        key = input("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37mNhập key của bạn: \033[1;33m")
        
        if key.startswith("BDQ_"):  # Kiểm tra định dạng key hợp lệ
            expiration_date = datetime.now() + timedelta(hours=12)  # Key có hạn 12 tiếng
            save_key(key, expiration_date)
            print("\033[1;32m✔ Key hợp lệ! Bạn có thể sử dụng tool.")
            break
        else:
            print("\033[1;31m✘ Key không hợp lệ, vui lòng nhập lại.")

# Main function
def main():
    os.system("cls" if os.name == "nt" else "clear")
    banner()
    
    # Kiểm tra key đã lưu, nếu hợp lệ thì bỏ qua nhập key
    if not check_saved_key():
        enter_key()

    show_tool_options()

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
