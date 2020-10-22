import pymem
import pymem.process
import time

dwSpeed = 0x00DA3C30
pm = pymem.Pymem("Among Us.exe")

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


if __name__ == "__main__":
    print("Wellcome to AMONG US SPEED HACK BY XSPHERE : \n")
    print("Current Speed Is :"+str(readAddressandSpeed()))
    sx = input("Enter Your Desired Speed : ")
    writeMemorySpeedx(sx)
    print("New Speed Is :"+str(readAddressandSpeed()))
