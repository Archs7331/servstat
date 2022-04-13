import os
import psutil
import subprocess
import json
import requests
import getpass

cores = psutil.cpu_count()
cpuload = str(round(float(os.popen('''top -n 1 -b | awk '/^%Cpu/{print $2}' ''').readline())))
cpu = subprocess.getoutput("grep -m 1 'model name' /proc/cpuinfo | cut -d: -f2 | sed -e 's/^ *//' | sed -e 's/$//'")
ram = subprocess.getoutput("free -m | grep -oP '\d+' | head -n 1")
ep1 = subprocess.getoutput("ip route get 1.2.3.4 | awk '{print $7}'")
uptime = subprocess.getoutput("uptime -p")
username = getpass.getuser()
ip = ep1.strip()
ip_api_response = requests.get(f"http://ip-api.com/json/{ip}?fields=as")
json_ip_data = json.loads(ip_api_response.text)
myasn = json_ip_data["as"]

if myasn == "AS16276 OVH SAS":
    print(f"""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   [38;2;87;136;241mCPU[0m: {cpu}
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   [38;2;87;136;241mCPU Cores[0m: {cores}
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   [38;2;87;136;241mRAM[0m: {ram}MB
@@@@@@@@@@@@@P[38;2;87;136;241m::::::::[0m!@@@@@@@@@   [38;2;87;136;241mUPTIME[0m: {uptime}
@![38;2;87;136;241m:[0mG@@@@@@@@P[38;2;87;136;241m::::::::[0m?@@@@@@G[38;2;87;136;241m:[0m!@   [38;2;87;136;241mCPU USAGE[0m: {cpuload}%
P[38;2;87;136;241m:::[0mP@@@@@@?[38;2;87;136;241m::::::::[0m?@@@@@@G[38;2;87;136;241m:::[0mP   [38;2;87;136;241mServer IP[0m: {ip}
![38;2;87;136;241m::::[0mP@@@@![38;2;87;136;241m::::::::[0mP@@GPPP?[38;2;87;136;241m::::[0m!   [38;2;87;136;241mUser[0m: {username}
[38;2;87;136;241m::::::[0m?@G![38;2;87;136;241m::::::::[0mG@@G[38;2;87;136;241m::::::::::[0m
?[38;2;87;136;241m:::::::::::::::[0mP@@@![38;2;87;136;241m::::::::::[0m?
G[38;2;87;136;241m::::::::::::::[0mG@@G???[38;2;87;136;241m:::::::::[0mG
@G[38;2;87;136;241m::::::::::::[0mG@@@@@@![38;2;87;136;241m::::::::[0mG@
@@G![38;2;87;136;241m::::::::[0m!@@@@@@@![38;2;87;136;241m:::::::[0m!G@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    """)
elif myasn == "AS396998 Path Network, Inc.":
    print(f"""
[+] Imagine using paf lmfao [+]
@@@@@@@@@@[34m????????????[0m@@@@@@@@@@   [34mCPU[0m: {cpu}
@@@@@@[34m???????????????????P[0m@@@@@@   [34mCPU Cores[0m: {cores}
@@@@[34m???????????GG???????????[0m@@@@   [34mRAM[0m: {ram}MB
@@[34m????????[0m@@@@@@@@@@@@[34m???????P[0m@@   [34mUptime[0m: {uptime}
@[34m??????G[0m@@@@@@@@@@@@@@@@P[34m??????[0m@   [34mCPU Usage[0m: {cpuload}%
@[34m?????[0m@@@@@@@[34m?????[0m@@@@@@@@[34m?????[0m@   [34mServer IP[0m: {ip}
[34m?????G[0m@@@@@[34m?????[0m@@@@@@@@@@[34m??????[0m   [34mUser[0m: {username}
[34m?????[0m@@@@@@[34m??????[0m@@@@@@@@@@[34m?????[0m
[34m?????[0m@@@@@@[34m??????????[0m@@@@@[34m??????[0m
@[34m????[0m@@@@@@@@[34m??????[0m@@@@@@@[34m?????[0m@
@[34m????[0m@@@@@@@@@@@@@@@@@@@[34m??????P[0m@
@@[34m???[0m@@@@@@@@@@@@@@@@@[34m???????G[0m@@
@@@@@@@@@@@[34m????PP???????????[0m@@@@
@@@@@@@@@@@[34m??????????????G[0m@@@@@@
@@@@@@@@@@@[34m???????????[0m@@@@@@@@@@
    """)
elif myasn == "AS53667 FranTech Solutions":
    print(f"""
[+] Imagine using paf lmfao [+]
@@@@@@@@@@[34m????????????[0m@@@@@@@@@@   [34mCPU[0m: {cpu}
@@@@@@[34m???????????????????P[0m@@@@@@   [34mCPU Cores[0m: {cores}
@@@@[34m???????????GG???????????[0m@@@@   [34mRAM[0m: {ram}MB
@@[34m????????[0m@@@@@@@@@@@@[34m???????P[0m@@   [34mUptime[0m: {uptime}
@[34m??????G[0m@@@@@@@@@@@@@@@@P[34m??????[0m@   [34mCPU Usage[0m: {cpuload}%
@[34m?????[0m@@@@@@@[34m?????[0m@@@@@@@@[34m?????[0m@   [34mServer IP[0m: {ip}
[34m?????G[0m@@@@@[34m?????[0m@@@@@@@@@@[34m??????[0m   [34mUser[0m: {username}
[34m?????[0m@@@@@@[34m??????[0m@@@@@@@@@@[34m?????[0m
[34m?????[0m@@@@@@[34m??????????[0m@@@@@[34m??????[0m
@[34m????[0m@@@@@@@@[34m??????[0m@@@@@@@[34m?????[0m@
@[34m????[0m@@@@@@@@@@@@@@@@@@@[34m??????P[0m@
@@[34m???[0m@@@@@@@@@@@@@@@@@[34m???????G[0m@@
@@@@@@@@@@@[34m????PP???????????[0m@@@@
@@@@@@@@@@@[34m??????????????G[0m@@@@@@
@@@@@@@@@@@[34m???????????[0m@@@@@@@@@@
    """)
elif myasn == "AS32751 Nuclearfallout Enterprises, Inc.":
    print(f"""
 [31m!!!!!!!!!!!!!!!!!!!!!!!!:!!!:[0m    [31mCPU[0m: {cpu}
 [31m!::::::::::::::::::P[0m@@@@@@@@@@[31m![0m  [31mCPU Cores[0m: {cores}
 [31m::::::::::::::![0m@@@[31m!::::::::[0m@@@[31m:[0m  [31mRAM[0m: {ram}MB
 [31m:::::::::::G[0m@@[31m::::::::::::[0m@@G[31m:[0m   [31mUptime[0m: {uptime}
 [31m:::::::::[0m@@[31m:::::::::::::?@[31m?:::[0m   [31mUptime[0m: {uptime}
 [31m[0m@:::::[0m@@[31m:::::[0m@@[31m:::::::[0m@@[31m::::::[0m   [31mCPU Usage[0m: {cpuload}%
 [31m::[0m@@[31m:[0m@[31m:::::::::::::[0m@@@[31m!:::::::[0m   [31mCPU Usage[0m: {cpuload}%
 [31m::::[0m@::[0mP@@@P[31m:::[0m@:::::::[0m@@@[31m::::[0m   [31mServer IP[0m: {ip}
 [31m::::::[0m@@@P[31m:::::::[0m!P@@@@@@![31m::::[0m   [31mUser[0m: {username}
 @@@@@@@@@  @@@@@@@@  @@@@@@@@?
 @@@:::?@@? @@@::::: :@@!:::@@@
 @@@    @@? @@@@@@@  :@@:   @@@
 @@@    @@? @@@@@@@  :@@:   @@@
 @@@    @@? @@@      :@@@@@@@@@
    """)
else:
    print(f"""
[38;2;87;136;241mCPU[0m: {cpu}
[38;2;87;136;241mCPU Cores[0m: {cores}
[38;2;87;136;241mRAM[0m: {ram}MB
[38;2;87;136;241mUPTIME[0m: {uptime}
[38;2;87;136;241mCPU USAGE[0m: {cpuload}%
[38;2;87;136;241mServer IP[0m: {ip}
[38;2;87;136;241mUser[0m: {username}
""")
