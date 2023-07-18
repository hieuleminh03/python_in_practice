from time import sleep

import os

from playsound import playsound

time = int(input("Nhap so giay: "))

while time > 0:
    # lam gi do
    
    # xoa man hinh
    os.system('cls')
    
    hour = time // 3600

    minute = (time % 3600) // 60

    second = time - hour*3600 - minute*60

    print("%02d : %02d : %02d" %(hour, minute, second))
    
    time -= 1
    
    sleep(1)
    
print("Time out!")

playsound("beep-01a.mp3")

