#Tool Reg Pro5
#Phạm Định Quốc
import random
from atexit import register
from time import sleep
import os,json,re,sys
import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests
os.system("clear")
dau="\033[1;32m~ [✓] => "
logo=f"""\x1b[31m╩╦══════════════════════════════╦╩

██╗  ██╗███╗   ██╗███████╗ ██████╗ ███╗   ██╗
╚██╗██╔╝████╗  ██║██╔════╝██╔═══██╗████╗  ██║
 ╚███╔╝ ██╔██╗ ██║█████╗  ██║   ██║██╔██╗ ██║
 ██╔██╗ ██║╚██╗██║██╔══╝  ██║   ██║██║╚██╗██║
██╔╝ ██╗██║ ╚████║███████╗╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝
                                             
\x1b[31m╦╩══════════════════════════════╩╦
 \x1b[38;5;231mAdmin\x1b[31m:   \x1b[38;5;231mPhamDinhQuoc
\x1b[31m╩╦══════════════════════════════╦╩
{dau}\033[1;31mTool Reg Page Pro5
{dau}\033[1;36mLink Facebook: \033[1;37mwww.facebook.com/PhamDinhQuoc.X.Profile
{dau}\033[1;33mZalo: \033[1;37m0865534267
{dau}\033[1;35mGithub: https://github.com/Pdquoc
\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"""
for h in logo:
       sys.stdout.write(h)
       sys.stdout.flush()
       sleep(0.0005)
import requests
from time import strftime

class reg_pro5():
    def __init__(self,cookies, name) -> None:
        self.cookies = cookies
        self.id_acc = self.cookies.split('c_user=')[1].split(';')[0]
        headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi',
            'cookie': self.cookies,
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'viewport-width': '1366',
        }
        url_profile = requests.get('https://www.facebook.com/me', headers=headers).url
        profile = requests.get(url_profile, headers=headers).text
        try:
            self.fb_dtsg = profile.split('{"name":"fb_dtsg","value":"')[1].split('"},')[0]
        except:
            self.fb_dtsg = profile.split(',"f":"')[1].split('","l":null}')[0]
    def Reg(self):
        
        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            # Requests sorts cookies= alphabetically
            'cookie': self.cookies,
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/pages/creation?ref_type=launch_point',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'viewport-width': '979',
            'x-fb-friendly-name': 'AdditionalProfilePlusCreationMutation',
            'x-fb-lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
        }

        data = {
            'av': self.id_acc,
            '__user': self.id_acc,
            '__a': '1',
            '__dyn': '7AzHxq1mxu1syUbFuC0BVU98nwgU29zEdEc8co5S3O2S7o11Ue8hw6vwb-q7oc81xoswIwuo886C11xmfz81sbzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK6E7e58jwGzE8FU5e7oqBwJK2W5olwuEjUlDw-wUws9ovUaU3qxWm2Sq2-azo2NwkQ0z8c84K2e3u362-2B0oobo',
            '__csr': 'gP4ZAN2d-hbbRmLObkZO8LvRcXWVvth9d9GGXKSiLCqqr9qEzGTozAXiCgyBhbHrRG8VkQm8GFAfy94bJ7xeufz8jK8yGVVEgx-7oiwxypqCwgF88rzKV8y2O4ocUak4UpDxu3x1K4opAUrwGx63J0Lw-wa90eG18wkE7y14w4hw6Bw2-o069W00CSE0PW06aU02Z3wjU6i0btw3TE1wE5u',
            '__req': 't',
            '__hs': '19296.HYP:comet_pkg.2.1.0.2.1',
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': '1006496476',
            '__s': '1gapab:y4xv3f:2hb4os',
            '__hsi': '7160573037096492689',
            '__comet_req': '15',
            'fb_dtsg': self.fb_dtsg,
            'jazoest': '25404',
            'lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
            '__aaid': '800444344545377',
            '__spin_r': '1006496476',
            '__spin_b': 'trunk',
            '__spin_t': '1667200829',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'AdditionalProfilePlusCreationMutation',
            'variables': '{"input":{"bio":"","categories":["181475575221097"],"creation_source":"comet","name":"'+name+'","page_referrer":"launch_point","actor_id":"'+self.id_acc+'","client_mutation_id":"1"}}',
            'server_timestamps': 'true',
            'doc_id': '5903223909690825',
        }
        
        response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)     
        try:
            return response.json()
        except:
                return response.text
os.system("clear")
print (logo)
dem = 0
ck = input ('\033[1;32m~ [✓] => \033[1;35mNhập Cookie Acc Reg Pro5 : ')  
dl =input('\033[1;32m~ [✓] => Nhập Delay Reg Pro5: ')
def delay(dl):
   t=datetime.now().strftime("%H:%M")
   for ti in range(int(dl) , 0, -1):
    print(dau,f'\033[1;31m🌸 Đang Delay Reg Pro5 > {ti} < Giây  ',end='\r')
    sleep(0.200)
    print(dau,f'\033[1;32m🌸 Đang Delay Reg Pro5 > {ti} < Giây  ',end='\r')
    sleep(0.200)
    print(dau,f'\033[1;33m🌸 Đang Delay Reg Pro5 > {ti} < Giây  ',end='\r')
    sleep(0.200)
    print(dau,f'\033[1;35m🌸 Đang Delay Reg Pro5 > {ti} < Giây  ',end='\r')
    sleep(0.200)
    print(dau,f'\033[1;36m🌸 Đang Delay Reg Pro5 > {ti} < Giây  ',end='\r')
    sleep(0.200)
cookies = (ck)#cookies acc cần reg (chỉ acc đang reg được pro5 mới dùng được):
while True:
    arrayho = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Võ", "Vũ", "Phan", "Trương", "Bùi", "Đặng", "Đỗ", "Ngô", "Hồ", "Dương", "Đinh"]
    arraylot = ["Công", "Đức", "Duy", "Gia", "Anh", "Hồng", "Đinh", "Quốc", "Quỳnh","Vĩnh"]
    arrayten = ["Hưng","Anh", "Văn", "Tuấn", "Hoàng", "Quốc", "Năm", "Giang", "Khang", "Dương", "Phúc", "Thiên", "Hùng", "Kiệt", "Châu", "Quỳnh", "huệ", "Tuấn", "Khánh", "Trân", "Yên", "Lợi", "Danh", "Vinh", "Nhi", "Nhí", "Quốc", "Anh", "Danh", "Hân", "Giang","Phán"]
    ho = random.choice(arrayho)
    lot = random.choice(arraylot)
    ten = random.choice(arrayten)
    name = str(ho+' '+lot+' '+ten)
    dem = dem+1
    print(dau,dem,reg_pro5(cookies, name).Reg())#kết quả trả về của api
    delay(dl);
        


