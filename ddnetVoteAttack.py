import os
import keyboard
import time
file_path = "C:\\Users\\Lenovo\\Downloads\\ddper-v8.1-win64\\DDPER.exe"
tedad = int(input("chand ta vote mikhay? "))
boo = input("f3 / f4 : ")
while tedad > 0:
    os.startfile(file_path)
    time.sleep(3)


    keyboard.press_and_release('enter')
    time.sleep(1)

    time.sleep(1)
    keyboard.press_and_release('enter')
    time.sleep(1)

    if boo == "f4":
        keyboard.press_and_release('F4')
        tedad -= 1
    elif boo == "f3":
        keyboard.press_and_release('F3')
        tedad -= 1
    else:
        print("f3 /f4 ra dobare vared konid")
        os.system("taskkill /f /im DDPER.exe")
        tedad = 0







