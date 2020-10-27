import pymem
import pymem.process
import psutil
import os
import time
class PymongUS:
    def __init__(self):
        self.dwspeed = 0x00DA3C30
        self.imposter =0x00DA5A84
        self.pm = pymem.Pymem('Among Us.exe')

    def makemeImposter(self):
        try:
            client = pymem.process.module_from_name(self.pm.process_handle,"GameAssembly.dll").lpBaseOfDll
            imp = self.pm.read_int(client+self.imposter)
            #print(hex(imp))
            off1 = self.pm.read_int(imp+0x5C)
            off2 = self.pm.read_int(off1+0x0)
            off3 = self.pm.read_int(off2+0x034)
            off4 = hex(off3+0x28)
            intoff4 = int(off4,16)
            self.pm.write_int(intoff4,1)
            return {"error":False,"Imposter":True}
        except Exception:
            return {"error":True,"Imposter":False}

    def changeSpeed(self,aspeed):
        try:
            client = pymem.process.module_from_name(self.pm.process_handle,"GameAssembly.dll").lpBaseOfDll
            speed = self.pm.read_int(client+self.dwspeed)
            off1 = self.pm.read_int(speed+0x5C)
            off2 = self.pm.read_int(off1+0x14)
            off3 = hex(off2+0x14)
            intva = int(off3, 16)
            self.pm.write_float(intva,float(aspeed))
            return {"error":False,"Speed":True}
        except Exception:
            return {"error":True,"Speed":False}

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    I was so bored i stole this function from :
    https://gist.github.com/Sanix-Darker/8cbed2ff6f8eb108ce2c8c51acd2aa5a
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


while True:
    if checkIfProcessRunning('Among Us'):
        print('[+] Among US Is Running\n[+]Initializing Pymong Please Wait...........')
        time.sleep(10)
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('[+] Waiting For Among US')

def intro():
    print("""
        ______                                  _   _ _____  
    | ___ \                                | | | /  ___| 
    | |_/ /   _ _ __ ___   ___  _ __   __ _| | | \ `--.  
    |  __/ | | | '_ ` _ \ / _ \| '_ \ / _` | | | |`--. \ 
    | |  | |_| | | | | | | (_) | | | | (_| | |_| /\__/ / 
    \_|   \__, |_| |_| |_|\___/|_| |_|\__, |\___/\____/  
        __/ |                       __/ |             
        |___/                       |___/              
        
            Python Sample Code For Memory Reading/Writing\n\n""")


if __name__ == "__main__":
    intro()
    app = PymongUS()
    print("[1] Change Speed \n[2] Access Imposter Feature : ")
    cheatOptions = int(input("Select your option either 1 or two : "))
    if cheatOptions == 1:
        speedtoset = float(input("        [+]Select Your Desired Speed : "))
        app.changeSpeed(speedtoset)
        print(f'        [+] Speed Changed!! Current Speed IS : {speedtoset}')
    elif cheatOptions == 2:
        app.makemeImposter()
        print('        [+] You Now Have Imposter Access')
