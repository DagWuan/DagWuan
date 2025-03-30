
import json
import requests, os, time
import socket
from time import strftime
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import time
import sys
banner = '\033[1;31m─────────────────────────────────────────────────────────\n\033[1;31m[\033[1;37m🌸\033[1;31m] \033[1;37m=> \033[1;33mTOOL GOLIKE TIKTOK \n\033[1;31m[\033[1;37m🌸\033[1;31m] \033[1;37m=> \033[1;35mADMIN: \033[1;36mDUYKHANH\n\033[1;31m[\033[1;37m🌸\033[1;31m] \033[1;37m=> \033[1;32mBOX SUPPORT: \033[1;37m https://zalo.me/g/nguadz335\n\033[1;31m[\033[1;37m🌸\033[1;31m] \033[1;37m=> \033[1;34mYOUTUBE: \033[1;37mREVIEWTOOL247NDK\n\033[1;31m───────────────────────────────────────────────────────── '
os.system('cls' if os.name == 'nt' else 'clear')
for x in banner:
    print(x, end='')
    sleep(0.001)
print('\x1b[1;31m🌸')    
try:
    Authorization = open('Authorization.txt', 'x')
    t = open('token.txt', 'x')
except:
    pass
Authorization = open('Authorization.txt', 'r')
t = open('token.txt', 'r')
author = Authorization.read()
token = t.read()
if author == '':
    author = input('\033[1;32mNHẬP AUTHORIZATION : ')
    token = input('\033[1;32mNHẬP T : ')
    Authorization = open('Authorization.txt', 'w')
    t = open('token.txt', 'w')
    Authorization.write(author)
    t.write(token)
else:
    select = input('\x1b[1;97m║ Đăng\x1b[1;96m Nhập \x1b[1;95mTài \x1b[1;94mKhoản \x1b[1;93mHiện \x1b[1;92mCó\x1b[1;91m ( Enter Để Bỏ Qua ,Nhập AUTHORIZATION Tại Đây \x1b[1;97m║\x1b[1;91m Để Đổi )  \n\x1b[1;97m╚⟩⟩⟩ ')
    if select != '':
        author = select
        token = input('\033[1;32m[1;36mNhập T : ')
        Authorization = open('Authorization.txt', 'w')
        t = open('token.txt', 'w')
        Authorization.write(author)
        t.write(token)
Authorization.close()
t.close()
headers = {'Accept': 'application/json, text/plain, */*', 'Content-Type': 'application/json;charset=utf-8', 'Authorization': author, 't': token, 'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36', 'Referer': 'https://app.golike.net/account/manager/tiktok'}

def chonacc():
    json_data = {}
    response = requests.get('https://gateway.golike.net/api/tiktok-account', headers=headers, json=json_data).json()
    return response

def nhannv(account_id):
    params = {'account_id': account_id, 'data': 'null'}
    json_data = {}
    response = requests.get('https://gateway.golike.net/api/advertising/publishers/tiktok/jobs', params=params, headers=headers, json=json_data).json()
    return response

def hoanthanh(ads_id, account_id):
    json_data = {'ads_id': ads_id, 'account_id': account_id, 'async': True, 'data': None}
    response = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs', headers=headers, json=json_data).json()
    return response

def baoloi(ads_id, object_id, account_id, loai):
    json_data1 = {'description': 'Tôi đã làm Job này rồi', 'users_advertising_id': ads_id, 'type': 'ads', 'provider': 'tiktok', 'fb_id': account_id, 'error_type': 6}
    response = requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1).json()
    json_data = {'ads_id': ads_id, 'object_id': object_id, 'account_id': account_id, 'type': loai}
    response = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs', headers=headers, json=json_data).json()
chontktiktok = chonacc()

def dsacc():
    if chontktiktok['status'] != 200:
        print('\033[1;31mAuthorization hoặc T sai hãy nhập lại!!!')
        quit()
    for i in range(len(chontktiktok['data'])):
        print(f'\x1b[1;97m[🌸]➭\x1b[1;36m [{i + 1}] \x1b[1;91m=> \x1b[1;97mTên Tài Khoản┊\x1b[1;32m :\x1b[1;93m {chontktiktok['data'][i]['nickname']}  ')
dsacc()
while True:
    try:
        luachon = int(input('\x1b[1;35m\x1b[1;97m║ Chọn \x1b[1;96mTài \x1b[1;95mKhoản \x1b[1;94mĐể \x1b[1;93mChạy \n\x1b[1;97m╚⟩⟩⟩ '))
        while luachon > len(chontktiktok['data']):
            luachon = int(input(' \033[1;31mAcc Này Không Có Trong Danh Sách , Hãy Nhập Lại : '))
        account_id = chontktiktok['data'][luachon - 1]['id']
        break
    except:
        print('\x1b[1;35mSai Định Dạng !!!')
while True:
    try:
        delay = int(input('\x1b[1;97m║ Nhập\x1b[1;91m Delay \n\x1b[1;97m╚⟩⟩⟩ '))
        break
    except:
        print('\x1b[1;31mSai Định Dạng !!!')
while True:
    try:
        doiacc = int(input('\x1b[1;97m║ \x1b[1;99mNhận\x1b[1;91m Tiền\x1b[1;96m Thất\x1b[1;95m Bại\x1b[1;94m Bao\x1b[1;93m Nhiu\x1b[1;92m Lần\x1b[1;91m Thì\x1b[1;96m Dừng\x1b[1;93m \n\x1b[1;97m╚⟩⟩⟩ '))
        break
    except:
        print('\x1b[1;31mNhập Vào 1 Số!!!')
os.system('cls' if os.name == 'nt' else 'clear')
dem = 0
tong = 0
checkdoiacc = 0
dsaccloi = []
accloi = ''
os.system('cls' if os.name == 'nt' else 'clear')
for x in banner:
    print(x, end='')
    sleep(0.001)
print('\x1b[1;31mTool Auto TikTok')
while True:
    if checkdoiacc == doiacc:
        dsaccloi.append(chontktiktok['data'][luachon - 1]['nickname'])
        print(f'\x1b[1;36mCác Acc Tiktok {dsaccloi} Có Vẻ Gặp Vấn Đề Nên Đổi Acc Chạy Đê ')
        dsacc()
        while True:
            try:
                luachon = int(input('\x1b[1;35m\x1b[1;97m║ Chọn \x1b[1;96mTài \x1b[1;95mKhoản \x1b[1;94mĐể \x1b[1;93mChạy \n\x1b[1;97m╚⟩⟩⟩  '))
                while luachon > len(chontktiktok['data']):
                    luachon = int(input('\x1b[1;32mAcc Này Không Có Trong Danh Sách, Hãy Nhập Lại : '))
                account_id = chontktiktok['data'][luachon - 1]['id']
                checkdoiacc = 0
                break
            except:
                print('\x1b[1;35mSai Định Dạng !!!')
    print(f'\x1b[1;97mĐang \x1b[1;96mLấy \x1b[1;95mNhiệm \x1b[1;91mVụ\x1b[1;93m Follow', end='\r')
    while True:
        try:
            nhanjob = nhannv(account_id)
            break
        except:
            pass
    if nhanjob['status'] == 200:
        ads_id = nhanjob['data']['id']
        link = nhanjob['data']['link']
        object_id = nhanjob['data']['object_id']
        if nhanjob['data']['type'] != 'follow':
            baoloi(ads_id, object_id, account_id, nhanjob['data']['type'])
            continue
        os.system(f'termux-open-url {link}')
        for remaining_time in range(delay, -1, -1):
            colors = ['\x1b[1;37mB\x1b[1;36mD\x1b[1;35mQ \x1b[1;32mT\x1b[1;31mO\x1b[1;34mO\x1b[1;33mL\x1b[1;31m\x1b[1;32m', '\x1b[1;34mB\x1b[1;31mD\x1b[1;37mQ \x1b[1;36mT\x1b[1;32mO\x1b[1;35mO\x1b[1;37mL\x1b[1;31m\x1b[1;32m', '\x1b[1;31mB\x1b[1;37mD\x1b[1;36mQ \x1b[1;33mT\x1b[1;35mO\x1b[1;32mO\x1b[1;34mL\x1b[1;31m\x1b[1;32m', '\x1b[1;32mB\x1b[1;33mD\x1b[1;34mQ \x1b[1;35mT\x1b[1;36mO\x1b[1;37mO\x1b[1;36mL\x1b[1;31m\x1b[1;32m', '\x1b[1;37mB\x1b[1;34mD\x1b[1;35mQ \x1b[1;36mT\x1b[1;32mO\x1b[1;33mO\x1b[1;31mL\x1b[1;31m\x1b[1;32m', '\x1b[1;34mB\x1b[1;33mD\x1b[1;37mQ \x1b[1;35mT\x1b[1;31mO\x1b[1;36mO\x1b[1;36mL\x1b[1;31m\x1b[1;32m', '\x1b[1;36mB\x1b[1;35mD\x1b[1;31mQ \x1b[1;34mT\x1b[1;37mO\x1b[1;35mO\x1b[1;32mL\x1b[1;31m\x1b[1;32m']
            for color in colors:
                print(f'\r{color}|{remaining_time}| \x1b[1;31m', end='')
                time.sleep(0.12)
        print('\r                          \r', end='')
        print('\x1b[1;35mĐang Nhận Tiền         ', end='\r')
        attempts = 0
        max_attempts = 2
        while attempts < max_attempts:
            try:
                nhantien = hoanthanh(ads_id, account_id)
                if nhantien['status'] == 200:
                    dem += 1
                    tien = nhantien['data']['prices']
                    tong += tien
                    local_time = time.localtime()
                    hour = local_time.tm_hour
                    minute = local_time.tm_min
                    second = local_time.tm_sec
                    h = f'{hour:02d}'
                    m = f'{minute:02d}'
                    s = f'{second:02d}'
                    chuoi = f'\x1b[1;31m\x1b[1;36m{dem}\x1b[1;31m\x1b[1;97m | \x1b[1;33m{h}:{m}:{s}\x1b[1;31m\x1b[1;97m | \x1b[1;32msuccess\x1b[1;31m\x1b[1;97m | \x1b[1;31m{nhantien['data']['type']}\x1b[1;31m\x1b[1;32m\x1b[1;32m\x1b[1;97m |\x1b[1;32m Ẩn ID\x1b[1;97m | \x1b[1;97m \x1b[1;32m+{tien} \x1b[1;97m| \x1b[1;33m{tong}'
                    print(' ' * 60, end='\r')
                    print(chuoi)
                    checkdoiacc = 0
                    break
                elif attempts == 0:
                    for countdown in range(3, -1, -1):
                        print(f'Vui lòng chờ {countdown} giây để hoàn thành job lần thứ 2', end='\r')
                        time.sleep(1)
                    print(' ' * 50, end='\r')
                attempts += 1
            except Exception as e:
                print(f'Đã xảy ra lỗi: {str(e)}. Thử lại lần {attempts + 1}.')
                attempts += 1
                time.sleep(1)
        if attempts == max_attempts:
            print('\x1b[1;31mBỏ Qua Nhiệm Vụ', end='\r')
            time.sleep(1)
        if nhantien['status'] != 200:
            while True:
                try:
                    baoloi(ads_id, object_id, account_id, nhanjob['data']['type'])
                    print(' ' * 60, end='\r')
                    print('\x1b[1;31mBỏ Qua Nhiệm Vụ', end='\r')
                    time.sleep(1)
                    checkdoiacc += 1
                    break
                except Exception as e:
                    print(f'Lỗi khi xử lý thông báo lỗi: {str(e)}')
                    time.sleep(1)
