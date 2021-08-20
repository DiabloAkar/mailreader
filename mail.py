import datetime
import time
from imap_tools import AND, mailbox
import threading
import imap_tools 
from pip._vendor.colorama import Fore
import subprocess
'import layn'
from imap_tools import MailBox

subprocess.call('start https://discord.gg/DDcXf472BF', shell=True)
subprocess.call('start https://github.com/DiabloAkar', shell=True)
subprocess.call('start pip install imap_tools', shell=True)


bammer = '''

████████▄   ▄█     ▄████████ ▀█████████▄   ▄█        ▄██████▄  
███   ▀███ ███    ███    ███   ███    ███ ███       ███    ███ 
███    ███ ███▌   ███    ███   ███    ███ ███       ███    ███ 
███    ███ ███▌   ███    ███  ▄███▄▄▄██▀  ███       ███    ███ 
███    ███ ███▌ ▀███████████ ▀▀███▀▀▀██▄  ███       ███    ███ 
███    ███ ███    ███    ███   ███    ██▄ ███       ███    ███ 
███   ▄███ ███    ███    ███   ███    ███ ███▌    ▄ ███    ███ 
████████▀  █▀     ███    █▀  ▄█████████▀  █████▄▄██  ▀██████▀  
                                          ▀                    

'''

print(Fore.YELLOW+bammer)
print(Fore.YELLOW)
print(Fore.YELLOW+"Instagram = diabloakar")
print(Fore.YELLOW+"Github = https://github.com/DiabloAkar")
print(Fore.YELLOW+"Sistem Hazırlanıyor")
time.sleep(1)
print('%1 [=                                       ]')
time.sleep(1)
print('%3 [===                                     ]')
time.sleep(1)
print('%10 [======                                  ]')
time.sleep(1)
print('%20 [========                                ]')
time.sleep(1)
print('%30 [=================                       ]')
time.sleep(1)
print('%40 [======================                  ]')
time.sleep(1)
print('%60 [=============================           ]')
time.sleep(1)
print('%70 [================================        ]')
time.sleep(1)
print('%90 [======================================  ]')
time.sleep(1)
print('%100 [========================================]')
time.sleep(1)

PostaKutusu = MailBox

PostaKutusu = MailBox('imap.gmail.com') # Buraya gmail girecekseniz gmail hotmail girecekseniz hotmail yapın.
PostaKutusu.login(kullanici, sifre, initial_folder="INBOX") # INBOX Yerine nereyi göstertmek istiyorsanız oraya girin.
# Burada kriter seçeceğiz örneğin 01.08.2021'den sonra gelen mesajları göster gibi


import datetime
from imap_tools import AND, mailbox
kr1ter = AND(date_g4te=datetime.date('2021,08,08'), from_= kullaniciadi)  # 2021,08,08 yerini istediğiniz tarihi giriniz.
for msg in PostaKutusu.fetch(kr1ter):
    print(msg.text)
