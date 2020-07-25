#imports 
import os 
import sys 
import time

#Art Not Realy Art Art Takes Time!
os.system("clear")
os.system("figlet BlueZsec")
print("|-----------------------|")
print("|   RE70-DECEMBER       |")
print("|  Team - BlueZsec      |")
print("|-----------------------|")
print("|_______________________|")
print("|[1]. Scan             |")
print("|[2]. Attack           |")
print("|[3]. Help             |")
print("|[4]. Exit             |")
print("|______________________|")
print("|                      |")

#menu
op = input("main_menu > ")
if op == "1":
  os.system("clear")
  os.system("hcitool scan")
  print("")
  print("[                    ] 0% ")
  time.sleep(5)
  print("[=====               ] 25%")
  time.sleep(5)
  print("[==========          ] 50%")
  time.sleep(5)
  print("[===============     ] 75%")
  time.sleep(5)
  print("[====================] 100%")
  time.sleep(3)
  os.system("clear")
  print("[*]Returning")
  time.sleep(2)
  os.system("clear")
  os.system("python3 blue.py")
elif op == "2":
  os.system("clear")
  mac = input("MAC_INPUT > ")
  os.system("sudo l2ping -f "+mac)
  print("[*]Returning")
  time.sleep(2)
  os.system("clear")
  os.system("python3 blue.py")
elif op == "3":
  print("Ctrl + c to end attack!")
  print("Scan For Targets Copy There Mac Adress Then l2ping will Jam there connection")
  print("To Learn How To Use This Python Script Watch RE70-DECEMBER on YouTube!")
elif op == "4":
  sys.exit
else:
  os.system("python3 blue.py")
