import pymem
import pymem.process
import psutil
import os
dwSpeed = 0x00DA3C30
dwImposter = 0x00DA5A84

pm = pymem.Pymem('Among Us.exe')

def readBaseAddress():
    client = pymem.process.module_from_name(pm.process_handle,"GameAssembly.dll").lpBaseOfDll
    speed = pm.read_int(client+dwSpeed)
    off1 = pm.read_int(speed+0x5C)
    off2 = pm.read_int(off1+0x14)
    off3 = hex(off2+0x14)
    return off3
def readAddressandSpeed():
    address=readBaseAddress()
    speed = pm.read_float(int(address, 16))
    return speed

def writeMemorySpeedx(val):
    addressx = readBaseAddress()
    intva = int(addressx, 16)
    new_speed = pm.write_float(intva,float(val))
    return 1

def accessImposterFeatures():
    client = pymem.process.module_from_name(pm.process_handle,"GameAssembly.dll").lpBaseOfDll
    speed = pm.read_int(client+dwImposter)
    off1 = pm.read_int(speed+0x5C)
    off2 = pm.read_int(off1+0x0)
    off3 = pm.read_int(off2+0x034)
    off4 = hex(off3+0x28)
    intoff4 = int(off4,16)
    access = pm.write_int(intoff4,1)
    return 'Acceesed'

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
    print("[1] Change Speed \n[2] Access Imposter Feature : ")
    cheatOptions = int(input("Select your option either 1 or two : "))
    if cheatOptions == 1:
        speedtoset = int(input("        [+]Select Your Desired Speed : "))
        writeMemorySpeedx(speedtoset)
        print('        [+] Speed Changed!! Current Speed IS : '+str(readAddressandSpeed()))
    elif cheatOptions == 2:
        accessImposterFeatures()
        print('        [+] You Now Have Imposter Access')
