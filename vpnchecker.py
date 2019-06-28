# Requirements: 
# Windows OS -- Os Specific Commands. 
# Python 3 to be installed on the Host Machine. #
# AZ PowerShell Module needs to be installed - "Install-Module -Name Az -AllowClobber"
# Powershell Execution Policy to be remote-signed 
# Powershell Credentials to be autosaved accross Powershell sessions: Enable-AzRmContextAutosave 
# Python Requirements in the requirements.txt == 'pip install -r requirements.txt'

import pymsteams
import os
import subprocess
import time
import sys
import datetime, threading
from apscheduler.schedulers.background import BackgroundScheduler
 
REFRESH_INTERVAL = 30 ## How often the checkhost() function is run
scheduler = BackgroundScheduler()
scheduler.start()
myTeamsMessage = pymsteams.connectorcard('') ### The TEams Channel you wanna post this to
host = '' ### The IP Host you wanna check. ### 

def checkhost(): ### pings the host when triggered - If all is well, nothing happens. Scheduler then runs again in (x)seconds. 
    p = os.system('ping ' + host)
    if p == 0: 
        print('Successful Pings: waiting 30s darlin...')
        return ### If a 5 pings timeout in a row, the scheudler is stopped, and destroy_and create function is run
    else:
        scheduler.remove_all_jobs()
        destroy_and_create()
       

def destroy_and_create():
    subprocess.Popen(['powershell.exe', '-ExecutionPolicy', 'Unrestricted', './removeVPN.ps1'], stdout=sys.stdout)  ## Remove Azure Connection
    time.sleep(30) ## Wait 30 seonds bit for the dust to settle
    subprocess.Popen(['powershell.exe', '-ExecutionPolicy', 'Unrestricted', './addVPN.ps1'], stdout=sys.stdout) ## Recreate Azure Connection
    time.sleep(30) ## Wait 30 seconds for VPN to try and come back alive.
    p = os.system('ping ' + host) ## check for VPN Tunnel Success IF not, a teams message is displayed
    if p == 0:
        myTeamsMessage.text("Sup Ya'll. The VPN Went Down, but It's back up now, No Worries, I destroyed and recreated the connection for ya. -- AzureVPN Bot from AZ-SAW-WIN10 ")
        myTeamsMessage.send()
        main()
    else:
        myTeamsMessage.text("Sup Ya'll, the Azure VPN went Down. I tried to bring it back up, but it won't come back up. I stopped Trying. ¯\_(ツ)_/¯ -- AzureVPN Bot from AZ-SAW-WIN10")
        myTeamsMessage.send()
        print('Vpn stayed down for 30 seconds after recreation. Stopped Script.')
        sys.exit()
        
def main():
    job = scheduler.add_job(checkhost, 'interval', seconds = REFRESH_INTERVAL)
    print('Scheduled')
    while True:
        time.sleep(1)

main()


