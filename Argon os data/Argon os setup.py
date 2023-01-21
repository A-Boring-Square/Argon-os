import time
import os
import keyboard
keyboard.press('f11')

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

print("""
[1] Continue Whith Setup
[2] Ive Already Done Setup
""")

setup = input("[?]: ")
if setup == '1':
    name = input(str("Please enter your User Name to be displayed: "))
    pas = input(str("Please enter your Pasword to Login: "))
    with open('User data/username.txt', 'w') as f:
        f.writelines(name)
    with open('User data/password.txt', 'w') as f:
        f.writelines(pas)
    print("Setup Complete")
    input("Press Enter To Close Window:")    
    
    
    
if setup == '2':
            login_pass = open('User data/password.txt')
            login_name = open('User data/username.txt')
            l_p = login_pass.read()
            l_n = login_name.read()
            
while True:
    login = input(str("Please Enter The Password To " + l_n + ": "))
    if login == l_p:
        os.startfile("home.py")
        break
    else:
        print("Wrong Password")