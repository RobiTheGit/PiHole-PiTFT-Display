# -*- coding: utf-8 -*-
# Import Python System Libraries
import time
import json
import subprocess
import os
import sys
# Import Requests Library
import requests
#Import Blinka
import digitalio
import board

ccodes = ['\033[1;37;40m', '\033[1;36;40m', '\033[1;35;40m', '\033[1;34;40m', '\033[1;33;40m', '\033[1;32;40m', '\033[1;31;40m']
white = ccodes[0] 
cyan = ccodes[1]
magenta = ccodes[2]
blue = ccodes[3]
yellow = ccodes[4]
green = ccodes[5]
red = ccodes[6]

API_TOKEN = "INSERT_API_KEY_HERE"
api_url = "http://localhost/admin/api.php?summaryRaw&auth="+API_TOKEN
os.system('tput civis')

# Add buttons as inputs
buttonA = digitalio.DigitalInOut(board.D23)
buttonA.switch_to_input()
buttonB = digitalio.DigitalInOut(board.D24)
buttonB.switch_to_input()
try:
    while True:
        os.system('tput civis')
        cmd = "hostname -I | cut -d\' \' -f1"
        IP = "IP: "+subprocess.check_output(cmd, shell=True).decode("utf-8")
        cmd = "hostname | tr -d \'\\n\'"
        HOST = subprocess.check_output(cmd, shell=True).decode("utf-8")
        cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
        CPU = subprocess.check_output(cmd, shell=True).decode("utf-8")
        cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%s MB  %.2f%%\", $3,$2,$3*100/$2 }'"
        MemUsage = subprocess.check_output(cmd, shell=True).decode("utf-8")
        cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%d GB  %s\", $3,$2,$5}'"
        Disk = subprocess.check_output(cmd, shell=True).decode("utf-8")
        cmd = "cat /sys/class/thermal/thermal_zone0/temp |  awk \'{printf \"CPU Temp: %.1f C\", $(NF-0) / 1000}\'" # pylint: disable=line-too-long

    # Pi Hole data!
        try:
            r = requests.get(api_url)
            data = json.loads(r.text)    
            DNSQUERIES = data['dns_queries_today']
            ADSBLOCKED = data['ads_blocked_today']
            CLIENTS = data['unique_clients']
        except KeyError:
            time.sleep(1)
            continue
        os.system('clear')
        if not buttonA.value:  # just button A pressed
            print(f'{yellow}{IP}')
            print(f'{HOST}')
            print(f'{green}Ads Blocked: {ADSBLOCKED}')
            print(f'Clients: {CLIENTS}')
            print(f'{cyan}CPU:  {CPU}')
            print(f'Mem:  {MemUsage}')
            print(f'{magenta}Disk:  {Disk}')
            print(f'DNS Queries: {DNSQUERIES}{white}')
        elif not buttonB.value:
            print(f'{yellow}Where is Loki?\nWhere is Levi?\n{green}Loki Doki and Levy Devy!\n{cyan}Oh no, the quick brown fox jumped over them while they were being lazy.{white}')
        else:
            os.system('clear')
        
        time.sleep(0.01)
except:
    os.system('tput cnorm')
    sys.exit(0)
