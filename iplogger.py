import requests  as reqs 
import socket , time 
from colorama import Fore , init
import sys
from scapy.all import ARP, Ether, srp
import selenium
init()

a1 = "                          ██╗██████╗▄▄▄▄▄██╗▄▄▄▄▄▄██████╗▄▄██████╗▄▄██████╗ ███████╗██████╗\n "
a2 = "                          ██║██╔══██╗░█░███║████░██╔═══██╗██╔════╝▄██╔════╝ ██╔════╝██╔══██╗\n "
a3 = "                          ██║██████╔╝▀▄▀███║████░██║█░███║██║█░███╗██║░▀███╗█████╗  ██████╔╝\n "
a4 = "                          ██║██╔═══╝█▄█▄███║████░██║█▄▄██║██║█▄███║██║▄█▄██║██╔══╝  ██╔══██╗\n "
a5 = "                          ██║██║▀▀▀▀▀▀▀▀▀███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║\n "
a6 = "                          ╚═╝╚═╝         ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝"
credit = "------  [+] Tool by @Eyad156 or Driplay -------\n"

asciiart = a1 + a2 + a3 + a4 + a5 + a6
print(Fore.GREEN + "\n",asciiart)
print(Fore.LIGHTBLUE_EX + "\n",credit)

try: 
    ip = socket.gethostbyname("www.google.com")
    print(Fore.LIGHTGREEN_EX + "# Internet : Active")    
except Exception as e:
    
    print(Fore.LIGHTRED_EX + "  !!No Internet !! \nExitting in 10 seconds")  
    time.sleep(10)
    exit()
print(Fore.LIGHTCYAN_EX + "")
url = "https://ipinfo.io"
print("1. Check your ip info ")
print("2. Check somene's ip info ")
print("3. Get ip of web  \n")
print("4. Get devices connected on Wifi")

choice = input("Choice (1 or 2 or 3) > ")

if choice == "1":
    print(Fore.LIGHTBLUE_EX + "\n****Your Ip Info****\n")
    resp = reqs.get(url)
    alldata = resp.json()
    
    IP = alldata.get('ip')
    CT = alldata.get('city')
    RG = alldata.get('region')
    CY = alldata.get('country')
    LOC = alldata.get('loc')
    POS = alldata.get('postal')
    TZ = alldata.get('timezone')
    
    print(Fore.LIGHTCYAN_EX + "IP Address :",IP)
    print("City :",CT)
    print("Region :",RG)
    print("Country :",CY)
    print("Location :",LOC)
    print("Postal Code :",POS)
    print("Time Zone :",TZ)

elif choice == "2":
    print(Fore.LIGHTBLUE_EX + "\n***Someone's Ip Info****\n")
    Sip = input("Enter ip address : ")
    url = url+"/"+Sip
    
    resp = reqs.get(url)
    alldata = resp.json()
    
    IP = alldata.get('ip')
    CT = alldata.get('city')
    RG = alldata.get('region')
    CY = alldata.get('country')
    LOC = alldata.get('loc')
    POS = alldata.get('postal')
    TZ = alldata.get('timezone')
    
    print(Fore.LIGHTCYAN_EX + "\nIP Address :",IP)
    print("City :",CT)
    print("Region :",RG)
    print("Country :",CY)
    print("Location :",LOC)
    print("Postal Code :",POS)
    print("Time Zone :",TZ)
elif choice == '3':
    enter_name = input(Fore.YELLOW + "Enter name of website (example.com) -> ")
    get = socket.gethostbyname(enter_name)
    print(Fore.WHITE+f"Ip of {get} : "+Fore.LIGHTGREEN_EX +get)
# elif choice == '4':
else:
    print("Invalid choice , input 1 or 2")    



input(Fore.RED + "Exit > ")
sys.exit()