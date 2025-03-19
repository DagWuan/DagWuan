import sqlite3
import random
import socket
import datetime
import time
import os
from colorama import init, Fore, Style

# Khởi tạo colorama để hỗ trợ màu sắc trên Windows
init(autoreset=True)

# Kết nối database
conn = sqlite3.connect("taixiu.db")
cursor = conn.cursor()

# Tạo bảng lưu thông tin người chơi
cursor.execute('''
    CREATE TABLE IF NOT EXISTS players (
        ip TEXT PRIMARY KEY,
        name TEXT,
        money INTEGER
    )
''')
conn.commit()

# Lấy địa chỉ IP
def get_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "Unknown"

# Hiển thị banner
def show_banner():
    os.system("cls" if os.name == "nt" else "clear")  # Xóa màn hình terminal
    print(Fore.CYAN + """
████████  ██████ ██ ██    ██ ██ ██    ██ 
╚══██╔══╝██╔══██╗██║╚██╗ ██╔╝██║██║   ██║
   ██║   ███████║██║ ╚███╔╝  ██║██║   ██║
   ██║   ██╔══██║██║ ██╔██╗  ██║██║   ██║
   ██║   ██║  ██║██║██╔╝ ╚██╗██║╚██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝   ╚═╝╚═╝ ╚═════╝ 

    """ + Style.RESET_ALL)

# Hiển thị thông tin người chơi
def show_info(name, money, ip):
    today = datetime.datetime.now().strftime("%d-%m-%Y")
    print(Fore.YELLOW + "╔" + "═" * 40 + "╗")
    print(Fore.YELLOW + f"║ {Fore.CYAN}👤 Người Chơi: {Fore.GREEN}{name:<25}{Fore.YELLOW}║")
    print(Fore.YELLOW + f"║ {Fore.CYAN}💰 Tiền Hiện Có: {Fore.GREEN}{money:,} VND{Fore.YELLOW}  ║")
    print(Fore.YELLOW + f"║ {Fore.CYAN}📅 Ngày: {Fore.GREEN}{today:<25}{Fore.YELLOW}║")
    print(Fore.YELLOW + f"║ {Fore.CYAN}🌐 IP: {Fore.GREEN}{ip:<25}{Fore.YELLOW}║")
    print(Fore.YELLOW + "╚" + "═" * 40 + "╝" + Style.RESET_ALL)

# Kiểm tra và cho vay tiền
def check_and_loan(name, money, ip):
    if money <= 0:
        while True:
            show_info(name, money, ip)  # Hiển thị thông tin trước khi hỏi vay
            try:
                loan = input(Fore.YELLOW + "\n💰 Vay Của Nhà Cái: (Nhập số tiền từ 1k đến 500k): ").replace("k", "000")
                loan = int(loan)
                
                if 1_000 <= loan <= 500_000:
                    money += loan
                    print(Fore.GREEN + f"💵 Người chơi {name} đã vay nhà cái {loan:,} VND!!")
                    cursor.execute("UPDATE players SET money=? WHERE ip=?", (money, ip))
                    conn.commit()
                    break
                else:
                    print(Fore.RED + "❌ Chỉ có thể vay từ 1,000 đến 500,000 VND! Vui lòng nhập lại.")
            except ValueError:
                print(Fore.RED + "❌ Vui lòng nhập số tiền hợp lệ!")

    return money

# Chơi tài xỉu
def play_game(name, money, ip):
    while True:
        show_info(name, money, ip)
        bet = input(Fore.CYAN + "🎲 Nhập số tiền cược (hoặc 'exit' để thoát): ").lower()
        if bet == "exit":
            print(Fore.RED + "Thoát game...")
            break

        # Xử lý nhập tiền
        try:
            bet = int(bet.replace("k", "000"))  # Đổi 1k -> 1000
            if bet > money or bet <= 0:
                print(Fore.RED + "❌ Số tiền không hợp lệ! Vui lòng nhập lại.")
                continue
        except ValueError:
            print(Fore.RED + "❌ Vui lòng nhập số hợp lệ!")
            continue

        # Chọn tài/xỉu
        choice = input(Fore.MAGENTA + "🎲 Xin mời bạn chọn (Tài/Xỉu): ").strip().lower()
        if choice not in ["tài", "xỉu", "tai", "xiu"]:
            print(Fore.RED + "❌ Lựa chọn không hợp lệ!")
            continue

        # Chuẩn hóa kết quả thành "Tài" hoặc "Xỉu"
        choice = "Tài" if choice in ["tài", "tai"] else "Xỉu"

        # Hiệu ứng gieo xúc xắc
        print(Fore.YELLOW + "\n⏳ Nhà cái sẽ lắc xúc xắc sau 3 giây...")
        for i in range(3, 0, -1):
            print(Fore.YELLOW + f"🎲 Xúc xắc đang gieo... {i}s")
            time.sleep(1)

        # Quay xúc xắc
        dice = [random.randint(1, 6) for _ in range(3)]
        total = sum(dice)
        result = "Tài" if total >= 11 else "Xỉu"

        print(Fore.CYAN + f"\n🎲 Xúc xắc: {dice} => Tổng: {total} => {Fore.GREEN if result == 'Tài' else Fore.RED}{result}")

        # Kiểm tra kết quả
        if choice == result:  
            money += bet * 2  # ✅ Nhân đôi tiền cược khi thắng
            print(Fore.GREEN + f"🎉 Bạn thắng! Nhận {bet * 2:,} VND. Tiền hiện có: {money:,} VND")
        else:
            money -= bet  # ❌ Mất đúng số tiền đã đặt cược
            print(Fore.RED + f"💸 Thua rồi :((( Tiền còn lại: {money:,} VND")

        # Kiểm tra nếu tiền về 0 => Hiển thị tùy chọn vay tiền
        money = check_and_loan(name, money, ip)

        # Cập nhật tiền trong database
        cursor.execute("UPDATE players SET money=? WHERE ip=?", (money, ip))
        conn.commit()

# Lấy thông tin người chơi hoặc tạo mới
def get_or_create_player():
    ip = get_ip()
    cursor.execute("SELECT name, money FROM players WHERE ip=?", (ip,))
    player = cursor.fetchone()

    if player:
        name, money = player
        print(Fore.GREEN + f"🎉 Chào mừng trở lại, {name}!")
    else:
        name = input(Fore.CYAN + "👤 Nhập tên người chơi: ")
        money = 100000  # 100k khi tạo mới
        cursor.execute("INSERT INTO players (ip, name, money) VALUES (?, ?, ?)", (ip, name, money))
        conn.commit()
        print(Fore.GREEN + f"✅ Tạo tài khoản mới cho {name} với 100k!")

    # Kiểm tra và xử lý vay tiền nếu cần
    money = check_and_loan(name, money, ip)

    return name, money, ip

# Chạy game
show_banner()
name, money, ip = get_or_create_player()
play_game(name, money, ip)

# Đóng kết nối
conn.close()
