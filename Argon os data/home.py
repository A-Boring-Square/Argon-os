import time
import os
import socket
import psutil
import keyboard
keyboard.press('f11')


battery = psutil.sensors_battery()
login_pass = open('User data/password.txt')
login_name = open('User data/username.txt')
l_p = login_pass.read()
l_n = login_name.read()
print("""
 ██        ██ ███████ ██       █████   █████  ███    ███ ███████   ████████  █████
 ██   ██   ██ ██      ██      ██   ██ ██   ██ ████  ████ ██           ██    ██   ██
  ██ ████ ██  █████   ██      ██      ██   ██ ██ ████ ██ █████        ██    ██   ██
  ████  ████  ██      ██      ██   ██ ██   ██ ██  ██  ██ ██           ██    ██   ██
  ██      ██  ███████ ███████  █████   █████  ██      ██ ███████      ██     █████


  █████  ██████   ██████   █████  ███   ██      █████   ██████
 ██   ██ ██   ██ ██       ██   ██ ████  ██     ██   ██ ██
 ███████ ██████  ██   ██  ██   ██ ██ ██ ██     ██   ██  █████
 ██   ██ ██   ██ ██    ██ ██   ██ ██  ████     ██   ██      ██
 ██   ██ ██   ██  ██████   █████  ██   ███      █████  ██████   ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴘʏᴛʜᴏɴ 
""")
print(" ")
print(" ")
print("WELCOME " + l_n)
print(" ")
print("The Date Is: " + time.strftime("%m/%d/%y"))
print(" ")
print("The Battery is at")
print(battery.percent)
print(" ")
print("valid commands are")
print("""
[1] Open Google
[2] Open Text Editor
[3] Open file explorer
[4] View Bios
[5] Games
""")
select = input("[?]: ")

if select == '1':
    os.startfile("browse.py")
    

if select == '2':
    os.startfile("text editor.py")
    
    
if select == '3':
    os.startfile("file explore.py")
    
    
if select == '4':
    while True:
        b_login = input(str("Please Enter The Password To " + l_n + " To open Bios: "))
        if b_login == l_p:
            print("Opening Bios")
            print(" ")
            host_name = socket.gethostname()
            host_ip = socket.gethostbyname_ex(host_name)
            print("USER NAME: " + l_n)
            print("PASSWORD: " + l_p)
            print("HOST NAME: ",host_name)
            print("ip address: ",host_ip)
            b = input("Press Enter To Close")
        else:
            print("Wrong Password")

if select == '5':
    os.startfile('games.py')