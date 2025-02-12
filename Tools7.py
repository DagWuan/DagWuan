import time
import os
import requests
import datetime
import hashlib
import sys
t = 3
t1 = 2
	
def loading(t):
	while t: 
		print('\033[1;36;40m loading \033[0m: ', t, end="\r") 
		time.sleep(1) 
		t -= 1

def chontool():
	import time
	def countdown(t1): 
		while t1: 
			print(' \033[1;36;40mLOADING\033[0m:', t1, end="\r") 
			time.sleep(1) 
			t1 -= 1
	countdown(int(t1))
	os.system('clear')
	print(" \033[1;34;40mCHỌN TOOL BẠN MUỐN SỬ DỤNG\033[0m")
	print("\033[1;36;40m [ \033[1;33;40m1\033[0m ] ♦ VUA THOÁT HIỂM ♚♦\033[0m[ \033[1;33;40mĐANG TRONG GIAI ĐOẠN PHÁT TRIỂN\033[0m ]")
	print("\033[1;36;40m [ \033[1;33;40m2\033[0m ] ♦ CHẠY ĐUA TỐC ĐỘ ♞♦\033[0m[ \033[1;33;40mĐANG TRONG GIAI ĐOẠN PHÁT TRIỂN\033[0m ]")
	print("\033[1;36;40m [ \033[1;33;40m3\033[0m ] ♦ HASH LOTTO ➑♦\033[0m")
	while True:
		x = str(input('\033[1;32;40m NHẬP TOOL BẠN MUỐN SỬ DỤNG: \033[0m'))
		if x == 'back':
			gioi_thieu()
			break
		elif x == '1':
			loading(t)
			print(" TOOL VẪN ĐANG TRONG QUÁ TRÌNH XÂY DỰNG VÀ TÌM HIỂU NGƯỜI CHƠI GẮNG ĐỢI NHÉ!")
			break
		elif x== '2':
			loading(t)
			print(" TOOL VẪN ĐANG TRONG QUÁ TRÌNH XÂY DỰNG VÀ TÌM HIỂU NGƯỜI CHƠI GẮNG ĐỢI NHÉ!")
			break
		elif x == '3':
			loading(t)
			chonlotto()
			break
		elif x == '4':
			os.system('exit')
			break
		else:
			print("\033[1;31;40m CÓ LỖI XẢY RA VUI LÒNG CHỌN LẠI ❌\033[0m")
			os.system('exit')
			break
				
def key():
	day = datetime.datetime.now().day
	key = hashlib.md5(f"{day}".encode()).hexdigest()
	url = f"https://webkey.x10.mx/?ma={key}"
	token = "6648c8f016f35d42cd052655" # Thay Token Của Bạn 
	try:
	    response = requests.get(f"https://link4m.co/api-shorten/v2", params={"api": token, "url": url}).json()
	    if response['status'] == "success":
	        link = response['shortenedUrl']
	    else:
	        print("Lỗi !!!")
	        sys.exit(27122010)
	except Exception as e:
	    sys.exit(e)
	def input_key():
		print('\033[1;36;40m ĐỢI VÀO TOOL \033[0m: ') 
		os.system('clear')
		print("\033[1;34;40m ██████╗ ███████╗████████╗ █████╗       ████████╗ █████╗  █████╗ ██╗\033[0m")
		print(" ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗      ╚══██╔══╝██╔══██╗██╔══██╗██║")
		print("\033[1;34;40m ██████╦╝█████╗     ██║   ███████║ █████╗  ██║   ██║  ██║██║  ██║██║\033[0m")
		print(" ██╔══██╗██╔══╝     ██║   ██╔══██║ ╚════╝  ██║   ██║  ██║██║  ██║██║")
		print("\033[1;34;40m ██████╦╝███████╗   ██║   ██║  ██║         ██║   ╚█████╔╝╚█████╔╝███████╗\033[0m")
		print(" ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝         ╚═╝    ╚════╝  ╚════╝ ╚══════╝")
		print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
		print("[📈] [\033[1;36;40m BETA - TOOL 1.2.2\033[0m ]")
		print("[🌸]\033[1;32;40m TOOL MADE BY :\033[0m [\033[1;33;40m NGUYỄN HOÀI SƠN \033[0m]")
		print("[🌸]\033[1;32;40m KÊNH TIK TOK:\033[0m [\033[1;33;40m @beta_tool \033[0m]")
		print("[🌸]\033[1;32;40m KÊNH YOUTUBE:\033[0m [\033[1;33;40m https://www.youtube.com/@beta_tool \033[0m]")
		print("[🌸]\033[1;32;40m ĐỊA CHỈ TELEGRAM:\033[0m [\033[1;33;40m @BETA_TOOL \033[0m]")
		print("[🌸]\033[1;32;40m GROUP NHẬN THÔNG BÁO:\033[0m [\033[1;33;40m https://t.me/Be_taTool \033[0m]")
		print("[🌸]\033[1;32;40m GROUP CỘNG ĐỒNG:\033[0m [\033[1;33;40m https://zalo.me/g/fgssum917 \033[0m]")
		print("[🌸]\033[1;32;40m SĐT ZALO:\033[0m [\033[1;33;40m 0969383118 \033[0m]")
		print("[🌸]\033[1;32;40m TK NGÂN HÀNG MB:\033[0m [\033[1;33;40m 0969383118 \033[0m]")
		print("[💵]\033[1;33;40m----------\033[0m\033[1;36;40mBẢNG GΙÁ TOOL ✅🔑\033[0m\033[1;33;40m----------\033[0m")
		print("[🌸]\033[1;32;40m ♦ FREE\033[0m     ➱➱➱➱ \033[1;33;40mKEY THƯỜNG\033[0m")
		print("[🌸]\033[1;32;40m ♦ 49.000₫\033[0m  ➱➱➱➱ \033[1;33;40mKEY BẠC/1 TOOL\033[0m")
		print("[🌸]\033[1;32;40m ♦ 119.000₫\033[0m ➱➱➱➱ \033[1;33;40mKEY VÀNG/ALL TOOL\033[0m")
		print("[🌸]\033[1;32;40m ♦ 259.000₫\033[0m ➱➱➱➱ \033[1;31;40mVĨNH VIỄN ĐƯỢC HỖ TRỢ UPDATE LIÊN TỤC\033[0m")
		print("[🌸]\033[1;32;40m CÁC KEY BẠC/VÀNG CHỈ CÓ T/D Ở BẢN UPDATE BẠN MUA THÔI NHÉ 🔥\033[0m")
		print("[🌸]\033[1;32;40m 🔥 ĐẢM BẢO NẾU TOOL THUA LỖ QUÁ NHIỀU SẴN SÀNG HOÀN 50% TRONG 3 DAY\033[0m")
		print("[🌸] ➱➱ \033[1;33;40mBẠN PHẢI CÓ BẰNG CHỨNG VÀ CÓ SỰ CHẤP THUẬN CỦA AD\033[0m")
		print("[🌸]\033[1;32;40m MUA KEY TOOL LH ADMIN QUA\033[0m \033[1;33;40mZALO HOẶC TELEGRAM ✅✅✅\033[0m")
		print(f"[🌸]\033[1;32;40m VƯỢT LINK ĐỂ CÓ KEY THƯỜNG ♦\033[0m: [\033[1;33;40m {link} \033[0m]")
		print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
		while True:
			inp = input("\033[1;36;40m NHẬP KEY 🔑 key = DangQuan  \033[0m: ")
			if inp == key:
				print("\033[1;32;40m KEY HỢP LỆ ✅\033[0m")
				open("key.txt", "w").write(inp)
				chontool()
				break
			elif inp == 'DangQuan':
				print("\033[1;32;40m KEY HỢP LỆ ✅\033[0m")
				open("key.txt", "w").write(inp)
				chontool()
				break
			else:
				print('\033[1;31;40m KEY LỖI VUI LÒNG KIỂM TRA LẠI ❌\033[0m')
				continue 
	
	if not os.path.exists("key.txt"):
	    input_key()
	else:
	    inp = open("key.txt", "r").read()
	    if inp == key:
	        pass
	    else:
	        input_key()
	
	
#lotto
import time
def lotto1():
	os.system('clear')
	print('\033[1;31;40m TOOL MADE BY\033[0m [ BETA - TOOL ]')
	print('\033[1;31;40m LOTTO\033[0m [ V1 ]')
	print(' [1] \033[1;36;40mNUÔI CẦU \033[0m')
	print(' [2] \033[1;36;40mNUÔI SỐ\033[0m [\033[1;33;40mĐANG TRONG GIAI ĐOẠN PHÁT TRIỂN\033[0m ]')
	print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
	while True:
		x = str(input("\033[1;32;40m NHẬP PHƯƠNG PHÁP CHƠI BẠN MUỐN \033[0m:"))
		if x == 'back':
			chonlotto()
		elif x == '1':
			os.system('clear')
			loading(t)
			print('\033[1;31;40m LOTTO\033[0m [ V1 ]')
			print('\033[1;31;40m HD AE CHƠI PHƯƠNG PHÁP NUÔI CẦU:\033[0m')
			print(' -\033[1;36;40m LẦN ĐẦU AE NGHE CÓ THỂ KHÔNG HIỂU NHƯNG PHƯƠNG PHÁP NUÔI CẦU\033[0m')
			print('\033[1;36;40m LÀ NUÔI NHỎ/HÒA/LỚN THEO TOOL CHỈ ĐỊNH\033[0m')
			print(' -\033[1;36;40m AE XEM KẾT QUẢ CỦA CÁC PHIÊN TRƯỚC TÌM PHẦN GIAO THOA\033[0m')
			print('\033[1;36;40m VD LỚN / NHỎ, HÒA / LỚN , HÒA / NHỎ , AE LẤY SỐ CỦA 2 PHIÊN ĐÓ NHẬP VÀO TOOL\033[0m')
			print(' -\033[1;36;40m VD TOOL CHỈ RA LỚN AE THEO TOOL ĐẶT LIÊN TIẾP 5 ROUND VÀO LỚN THEO LỚN, NHỎ THEO NHỎ\033[0m')
			print('\033[1;36;40m HÒA THEO HÒA ĐẾN KHI NÀO ĂN HOẶC THUA TOÀN BỘ 5 ROUND THÌ DỪNG CHƠI\033[0m')
			print('-\033[1;36;40m KHUYÊN AE KHỞI ĐẦU ĐẶT LÀ 100 BUILD / 0.1 UDST/WH\033[0m')
			print('-\033[1;36;40m MỖI LẦN GÃY AE X2 LÊN\033[0m')
			print('\033[1;36;40m VD 100 BUILD -> 200 BUILD/ 0.1 USDT/WH -> 0.2 USDT/WH\033[0m')
			print('\033[1;36;40m TIẾP 200 BUILD -> 400 BUILD/ 0.2 USDT/WH -> 0.4 USDT/WH\033[0m')
			print('-\033[1;36;40m LIÊN TỤC X2 LÊN ĐẾN KHI NÀO AE WIN HOẶC CHUỖI THUA CẢ 5 ROUND AE BÁO LẠI TOOL\033[0m')
			print('-\033[1;36;40m KHUYẾN KHÍCH AE NÀO GIÀU (SỐ DƯ TỪ > 5000 BUILD / > 3 USDT / > 3 WH)\033[0m')
			print('\033[1;36;40m MỚI NÊN THỬ SỨC VÌ TOOL TỈ LỆ ĂN CŨNG CHƯA CAO VÌ LÀ PHIÊN BẢN ĐẦU TIÊN\033[0m')
			print(' \033[1;32;40mLINK VIDEO HD CHƠI CHO AE NÀO KHÔNG HIỂU NHA\033[0m:')
			print('[ https://youtu.be/GJL63JTuQGM?si=Z7qOkb39OvPMba74 ]')
			countdown(T2)
			thuat_toan()
			
			break
		elif x == '2':
			os.system('clear')
			loading(t)
			print('\033[1;31;40m HD AE CHƠI PHƯƠNG PHÁP NUÔI SỐ:\033[0m')
			print('\033[1;36;40m - NUÔI SỐ LÀ TOOL SẼ HIỆN THỊ 3 MÀU XANH / VÀNG /  ĐỎ \033[0m')
			print('\033[1;36;40m THEO TỈ LỆ HÚP TỪ 90 % -> 60 % -> 30% ĐỂ AE ĐẶT THEO\033[0m')
			print('\033[1;36;40m - AE ĐẶT BUILD/USDT/WH THEO MÀU XANH VÀ VÀNG KHÔNG KHUYẾN ĐẶT ĐỎ\033[0m')
			print('\033[1;36;40m - AE ĐẶT TỪ 100 -> 200 BUILD / 0,01 - 0.1 USDT/WH\033[0m')
			print('\033[1;36;40m - AE CHƠI 7 ROUND HÚP THÌ AE BÁO TOOL GÃY THÌ AE NÊN NGHỈ\033[0m')
			break
		#toollotto3
		else:
			print('\033[7;30;41m LỖI VUI LÒNG KIỂM TRA LẠI CHƯƠNG TRÌNH BẠN MUỐN CHỌN❌\033[0m')
			os.system('exit')
			break

#lottov2
def lotto2():
	os.system('clear')
	print('\033[1;31;40m TOOL MADE BY\033[0m [ BETA - TOOL ]')
	print('\033[1;31;40m LOTTO\033[0m [ V2 ]')
	print(' [1] \033[1;36;40mNUÔI CẦU \033[0m')
	print(' [2] \033[1;36;40mNUÔI SỐ\033[0m [\033[1;33;40mĐANG TRONG GIAI ĐOẠN PHÁT TRIỂN\033[0m ]')
	print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
	while True:
		x = str(input("\033[1;32;40m NHẬP PHƯƠNG PHÁP CHƠI BẠN MUỐN \033[0m:"))
		if x == '1':
			os.system('clear')
			loading(t)
			print('\033[1;31;40m HD AE CHƠI PHƯƠNG PHÁP NUÔI CẦU:\033[0m')
			print(' -\033[1;36;40m LẦN ĐẦU AE NGHE CÓ THỂ KHÔNG HIỂU NHƯNG PHƯƠNG PHÁP NUÔI CẦU\033[0m')
			print('\033[1;36;40m LÀ NUÔI NHỎ/HÒA/LỚN THEO TOOL CHỈ ĐỊNH\033[0m')
			print(' -\033[1;36;40m AE XEM KẾT QUẢ CỦA CÁC PHIÊN TRƯỚC TÌM 3 CẦU LIÊN TIẾP GẦN NHAU NHẤT\033[0m')
			print('\033[1;36;40m SAU ĐÓ NHẬP VÀO TOOL\033[0m')
			print(' -\033[1;36;40m VD TOOL CHỈ RA LỚN AE THEO TOOL ĐẶT LIÊN TIẾP 5 ROUND VÀO LỚN THEO LỚN, NHỎ THEO NHỎ\033[0m')
			print('\033[1;36;40m HÒA THEO HÒA ĐẾN KHI NÀO ĂN HOẶC THUA TOÀN BỘ 5 ROUND THÌ DỪNG CHƠI\033[0m')
			print('-\033[1;36;40m KHUYÊN AE KHỞI ĐẦU ĐẶT LÀ 100 BUILD / 0.1 UDST/WH\033[0m')
			print('-\033[1;36;40m MỖI LẦN GÃY AE X2 LÊN\033[0m')
			print('\033[1;36;40m VD 100 BUILD -> 200 BUILD/ 0.1 USDT/WH -> 0.2 USDT/WH\033[0m')
			print('\033[1;36;40m TIẾP 200 BUILD -> 400 BUILD/ 0.2 USDT/WH -> 0.4 USDT/WH\033[0m')
			print('-\033[1;36;40m LIÊN TỤC X2 LÊN ĐẾN KHI NÀO AE WIN HOẶC CHUỖI THUA CẢ 5 ROUND AE BÁO LẠI TOOL\033[0m')
			print('-\033[1;36;40m KHUYẾN KHÍCH AE NÀO GIÀU SỐ DƯ TỪ > 5000 BUILD / > 3 USDT / > 3 WH\033[0m')
			print(' \033[1;32;40mKHUYÊN AE NÊN CHƠI VÀO KHUNG GIỜ PHIÊN 9h SÁNG 14h VỚI 8h TỐI CẦU SẼ KHÁ LÀ ĐẸP\033[0m')
			print(' \033[1;32;40mLINK VIDEO HD CHƠI CHO AE NÀO KHÔNG HIỂU NHA\033[0m:')
			print('[  https://youtu.be/kqV7LGSSNj8?si=6-vhTOS5vHkoJuuV ]')
			countdown(T2)
			thuat_toan1()
			
			break
		elif x == '2':
			os.system('clear')
			loading(t)
			print('\033[1;31;40m HD AE CHƠI PHƯƠNG PHÁP NUÔI SỐ:\033[0m')
			print('\033[1;36;40m - NUÔI SỐ LÀ TOOL SẼ HIỆN THỊ 3 MÀU XANH / VÀNG /  ĐỎ \033[0m')
			print('\033[1;36;40m THEO TỈ LỆ HÚP TỪ 90 % -> 60 % -> 30% ĐỂ AE ĐẶT THEO\033[0m')
			print('\033[1;36;40m - AE ĐẶT BUILD/USDT/WH THEO MÀU XANH VÀ VÀNG KHÔNG KHUYẾN ĐẶT ĐỎ\033[0m')
			print('\033[1;36;40m - AE ĐẶT TỪ 100 -> 200 BUILD / 0,01 - 0.1 USDT/WH\033[0m')
			print('\033[1;36;40m - AE CHƠI 7 ROUND HÚP THÌ AE BÁO TOOL GÃY THÌ AE NÊN NGHỈ\033[0m')
			break
		#toollotto3
		else:
			print('\033[7;30;41m LỖI VUI LÒNG KIỂM TRA LẠI CHƯƠNG TRÌNH BẠN MUỐN CHỌN❌\033[0m')
			os.system('exit')
			break


#cooldownlotto1
T2 = 10
v = 60
def thuat_toan1():
	X = str(input('\033[1;32;40m NẾU AE SẴN SÀNG CHƠI THÌ VUI LÒNG NHẬP\033[0m [\033[1;33;40m SS \033[0m] \033[1;32;40mĐỂ VÀO TOOL\033[0m: '))
	if X == 'SS':
		lotto()
	else:
		print('\033[1;31;40m LỖI TOOL CHỈ NHẬN\033[0m [\033[1;33;40m SS \033[0m]')
		thuat_toan1()

def thuat_toan():
	X = str(input('\033[1;32;40m NẾU AE SẴN SÀNG CHƠI THÌ VUI LÒNG NHẬP\033[0m [\033[1;33;40m SS \033[0m] \033[1;32;40mĐỂ VÀO TOOL\033[0m: '))
	if X == 'SS':
		lottofree()
	else:
		print('\033[1;31;40m LỖI TOOL CHỈ NHẬN\033[0m [\033[1;33;40m SS \033[0m]')
		thuat_toan()
		

def countdown(T2):
  while T2:
      mins, secs = divmod(T2, 60)  #tách phút và giây từ biến t
      timeformat = '{:02d}:{:02d}'.format(mins, secs) #định dạng thời gian hiển thị đếm ngược
      print(' \033[1;33;40mVUI LÒNG ĐỌC HD TRƯỚC KHI CHƠI \033[0m:', timeformat, end='\r') #hiển thị thời gian đếm ngược
      time.sleep(1) # chờ 1s và update thời gian
      T2 -= 1  #đếm ngược từng giây cho tới
      
def count_down2(v):
  while v:
      mins, secs = divmod(v, 60)  #tách phút và giây từ biến t
      timeformat = '{:02d}:{:02d}'.format(mins, secs) #định dạng thời gian hiển thị đếm ngược
      print('LOADING :', timeformat, end='\r') #hiển thị thời gian đếm ngược
      time.sleep(1) # chờ 1s và update thời gian
      v -= 1  #đếm ngược từng giây cho tới 
	
#lotto
def lottofree():
	import os
	os.system('clear')
	print('\033[1;31;40m TOOL MADE BY\033[0m [ BETA - TOOL ]')
	print('\033[1;31;40m LOTTO\033[0m [ V1 ]')
	print('\033[1;32;40m NHẬP 2 ROUND GIAO NHAU Ở LỊCH SỬ PHIÊN GẦN NHẤT : \033[0m')
	x = int(input('\033[1;35;40m PHIÊN ĐẦU : \033[0m'))
	y = int(input('\033[1;35;40m PHIÊN THỨ 2 : \033[0m'))
	kq = (x+y)/2
	if 18 < x > 3 and 3 < y > 18:
	    print('\033[1;31;40m LỖI ❌ NHẬP LẠI THEO HƯỚNG DẪN CHƠI \033[0m')
	    lottofree1()
	elif x <= 9 and y == 10 or x <= 9 and y == 11 and y <= 9 and x == 10 or y <= 9 and x == 11:
		print('\033[1;31;40m🔥CẢNH BÁO ĐÂY LÀ PHIÊN HÒA/NHỎ HOẶC NHỎ/HÒA TỈ LỆ BỊP CAO KHUYÊN NÊN QUAN SÁT KHÔNG ĐẶT🔥\033[0m')
		lottofree1()
	elif 10 < kq < 11:
	    print('\033[1;36;40m ♦ ĐÁNH HÒA TRONG 5 PHIÊN ♦\033[0m')
	    print('\033[1;32;40m HÒA RẤT KHÓ HÚP, NẾU QUÁ 3 -> 5 ROUND CHƯA HÚP THÌ NÊN BỎ \033[0m')
	elif kq >= 11:
	    print('\033[1;36;40m ♦ ĐÁNH LỚN TRONG 5 PHIÊN ♦\033[0m')
	elif kq <= 10:
		print('\033[1;36;40m ♦ ĐÁNH NHỎ TRONG 5 PHIÊN ♦\033[0m')
	else:
		print('LỖI❌')
		lottofree1()
	X = str(input(' NHẬP KẾT QUẢ SAU 5 ROUND NUÔI [WIN/LOSS] [DỪNG CHƠI THÌ NHẬP <BACK>]: '))
	if X == 'WIN':
	  print('\033[1;32;40m CHÚC MỪNG NGƯỜI CHƠI CHỐT LÃI THÀNH CÔNG ✅\033[0m')
	  os.system('cd /sdcard/BETATOOL[1.1.3] && python egs.py')
	elif X == 'LOSE':
	  print('\033[7;30;41m ADMIN KHUYÊN BẠN DỪNG CHƠI VÌ CÓ THẾ NHÀ CÁI BỊP HOẶC DO NHÂN PHẨM BẠN KÉM\033[0m')
	  os.system('cd /sdcard/BETATOOL[1.1.3] && python egs.py')
	elif X == 'BACK':
	  print('\033[1;34;40m CẢM ƠN BẠN ĐÃ SỬ DỤNG TOOL\033[0m')
	  os.system('exit')
	else:
	  print('\033[1;31;40m LỖI ❌ CHỈ ĐƯỢC NHẬP WIN / LOSE HOẶC BACK TOOL MỚI NHẬN\033[0m')
	  lottofree1()

def lottofree1():
	print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
	print('\033[1;31;40m TOOL MADE BY\033[0m [ BETA - TOOL ]')
	print('\033[1;31;40m LOTTO\033[0m [ V1 ]')
	print('\033[1;32;40m NHẬP 2 ROUND GIAO NHAU Ở LỊCH SỬ PHIÊN GẦN NHẤT : \033[0m')
	x = int(input('\033[1;35;40m PHIÊN ĐẦU : \033[0m'))
	y = int(input('\033[1;35;40m PHIÊN THỨ 2 : \033[0m'))
	3 > x < 18 and 3 > y < 18
	kq = (x+y)/2
	if x  < 3 and y > 18 or x > 18 and y < 3 or kq < 6 and kq > 14.5:
	    print('\033[1;31;40m LỖI ❌ NHẬP LẠI THEO HƯỚNG DẪN CHƠI \033[0m')
	    lottofree1()
	elif x <= 9 and y == 10 or x <= 9 and y == 11 and y <= 9 and x == 10 or y <= 9 and x == 11:
		print('\033[1;31;40m🔥CẢNH BÁO ĐÂY LÀ PHIÊN HÒA/NHỎ HOẶC NHỎ/HÒA TỈ LỆ BỊP CAO KHUYÊN NÊN QUAN SÁT KHÔNG ĐẶT🔥\033[0m')
		lottofree1()
	elif 10 < kq < 11:
	    print('\033[1;36;40m ♦ ĐÁNH HÒA TRONG 5 PHIÊN ♦\033[0m')
	    print('\033[1;32;40m HÒA RẤT KHÓ HÚP, NẾU QUÁ 3 -> 5 ROUND CHƯA HÚP THÌ NÊN BỎ \033[0m')
	elif kq >= 11:
	    print('\033[1;36;40m ♦ ĐÁNH LỚN TRONG 5 PHIÊN ♦\033[0m')
	elif kq <= 10:
		print('\033[1;36;40m ♦ ĐÁNH NHỎ TRONG 5 PHIÊN ♦\033[0m')
	else:
		print('LỖI❌')
		lottofree1()
	X = str(input(' NHẬP KẾT QUẢ SAU 5 ROUND NUÔI [WIN/LOSS] [DỪNG CHƠI THÌ NHẬP <BACK>]: '))
	if X == 'WIN':
	  print('\033[1;32;40m CHÚC MỪNG NGƯỜI CHƠI CHỐT LÃI THÀNH CÔNG ✅\033[0m')
	  lottofree1()
	elif X == 'LOSE':
	  print('\033[7;30;41m ADMIN KHUYÊN BẠN DỪNG CHƠI VÌ CÓ THẾ NHÀ CÁI BỊP HOẶC DO NHÂN PHẨM BẠN KÉM\033[0m')
	  lottofree1()
	elif X == 'BACK':
	  print('\033[1;34;40m CẢM ƠN BẠN ĐÃ SỬ DỤNG TOOL\033[0m')
	  os.system('exit')
	else:
	  print('\033[1;31;40m LỖI ❌ CHỈ ĐƯỢC NHẬP WIN / LOSE HOẶC BACK TOOL MỚI NHẬN\033[0m')
	  lottofree1()
	

def lotto():
	import os
	os.system('clear')
	print('\033[1;31;40m TOOL MADE BY\033[0m [ BETA - TOOL ]')
	print('\033[1;31;40m LOTTO\033[0m [ V2 ]')
	print('\033[1;32;40m NHẬP 3 ROUND GIAO NHAU Ở LỊCH SỬ PHIÊN GẦN NHẤT : \033[0m')
	x = int(input('\033[1;35;40m PHIÊN ĐẦU : \033[0m'))
	y = int(input('\033[1;35;40m PHIÊN THỨ 2 : \033[0m'))
	z = int(input('\033[1;35;40m PHIÊN THỨ 3 : \033[0m'))
	kq = (x+y+z)/3
	if 3 < x > 18 or 3 < y > 18 or 3 < z > 18:
		print('LỖI❌')
	elif 9.7 < kq < 10.7:
		print('\033[1;36;40m ♦ ĐÁNH HÒA TRONG 5 PHIÊN ♦\033[0m')
		count_down2(v)
		kq_lotto()
	elif kq >= 10.7:
		print('\033[1;36;40m ♦ ĐÁNH LỚN TRONG 5 PHIÊN ♦\033[0m')
		count_down2(v)
		kq_lotto()
	elif kq <= 9.7:
		print('\033[1;36;40m ♦ ĐÁNH NHỎ TRONG 5 PHIÊN ♦\033[0m')
		count_down2(v)
		kq_lotto()
	elif kq == 21 or kq == 20.5:
		print('\033[1;36;40m ♦ ĐÁNH NHỎ TRONG 5 PHIÊN ♦\033[0m')
		count_down2(v)
		kq_lotto()
	else:
		print('LỖI❌')
		lot_to()
	
def lot_to():
	print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
	print('\033[1;31;40m TOOL MADE BY\033[0m [ BETA - TOOL ]')
	print('\033[1;31;40m LOTTO\033[0m [ V2 ]')
	print('\033[1;32;40m NHẬP 3 ROUND GIAO NHAU Ở LỊCH SỬ PHIÊN GẦN NHẤT : \033[0m')
	x = int(input('\033[1;35;40m PHIÊN ĐẦU : \033[0m'))
	y = int(input('\033[1;35;40m PHIÊN THỨ 2 : \033[0m'))
	z = int(input('\033[1;35;40m PHIÊN THỨ 3 : \033[0m'))
	kq = (x+y+z)/3
	if 3 < x > 18 or 3 < y > 18 or 3 < z > 18:
		print('LỖI❌')
	elif 9.7 < kq < 10.7:
		print('\033[1;36;40m ♦ ĐÁNH HÒA TRONG 5 PHIÊN ♦\033[0m')
		count_down2(v)
		kq_lotto()
	elif kq >= 10.7:
		print('\033[1;36;40m ♦ ĐÁNH LỚN TRONG 5 PHIÊN ♦\033[0m')
		count_down2(v)
		kq_lotto()
	elif kq <= 9.7:
		print('\033[1;36;40m ♦ ĐÁNH NHỎ TRONG 5 PHIÊN ♦\033[0m')
		count_down2(v)
		kq_lotto()
	elif kq == 21 or kq == 20.5:
		print('\033[1;36;40m ♦ ĐÁNH NHỎ TRONG 5 PHIÊN ♦\033[0m')
		count_down2(v)
		kq_lotto()
	else:
		print('LỖI❌')
		lot_to()

def kq_lotto():
	X = str(input(' NHẬP KẾT QUẢ SAU 5 ROUND NUÔI [WIN/LOSS] [DỪNG CHƠI THÌ NHẬP <BACK>]: '))
	if X == 'WIN':
		print('\033[1;32;40m CHÚC MỪNG NGƯỜI CHƠI CHỐT LÃI THÀNH CÔNG ✅\033[0m')
		lot_to()
	elif X == 'LOSE':
		print('\033[7;30;41m ADMIN KHUYÊN BẠN DỪNG CHƠI VÌ CÓ THẾ NHÀ CÁI BỊP HOẶC DO NHÂN PHẨM BẠN KÉM\033[0m')
		lot_to()
	elif X == 'BACK':
		print('\033[1;34;40m CẢM ƠN BẠN ĐÃ SỬ DỤNG TOOL\033[0m')
		os.system('exit')
	else:
		print('\033[1;31;40m LỖI ❌ CHỈ ĐƯỢC NHẬP WIN / LOSE HOẶC BACK TOOL MỚI NHẬN\033[0m')
		lot_to()
		
#lottov1
def chonlotto():
	print('  \033[1;36;40m [ \033[1;33;40m1\033[0m ]  LOTTO V1 [ FREE ]')
	print('  \033[1;36;40m [ \033[1;33;40m2\033[0m ]  LOTTO V2 [ MẤT PHÍ 💵 ]')
	x = str(input('\033[1;35;40m  CHỌN PHIÊN BẢN LOTTO🔥 : \033[0m'))
	if x == 'back':
		gioi_thieu()
	if x == '1':
		lotto1()
	elif x == '2':
		x = str(input('\033[1;35;40m  NHẬP KEY ĐƯỢC CẤP CỦA ADMIN🔥🔥NHẬP: KHANHDZAI : \033[0m'))
		if x == 'KHANHDZAI': #keyvip
			lotto2()
		else:
			print(' LH MUA TOOL CHO AD NHÉ🔥')
			chonlotto()
	else:
		print('LỖI❌')
		chonlotto()

#code
if __name__ == '__main__':
	key()
	 
