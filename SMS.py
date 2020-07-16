#SMS SENDER by p0isonBR
import os
os.system('cls' if os.name == 'nt' else 'clear')
print("                            /+osyhhhhhhyys++/                            ")
print("                         +oydddhhhhyyhhhhdddhy+/                         ")
print("                      /+yddhyyyysssssssssyyyhddhs/                       ")
print("                     +hddyyssssssssssssssssssyyhdds/                     ")
print("                   /sddhyyyyyyssssssssssssssyyyyyhmh+                    ")
print("                  /hmdhhddddddhhhyyyyyyhhhhdddddhhhddo                   ")
print("                 /hmmdhs+/ //+osyhhhhhhysso+////ohddmdo                  ")
print("                /hmmmy.           `````          `smddd+                 ")
print("                smddm/     `````          `````   mdhmh/                 ")
print("               +ddydm+  -/osyyyys+.    ./syyyyso/-mdydms                 ")
print("               ymhyhmh.yyo/ -- +hdo  /dho -- /oyh.ymdyymd/               ")
print("              /dmyyymd.  ``.-   ./   -/.-   .``  `dmhsydmo               ")
print("              smdysymd   shdhyydy      sdyyhddy   dmyyshmy               ")
print("              dmysshmy                            smhssymd/              ")
print("             /dmyssymd                            hmhsyymm/              ")
print("             /dmyssyhms                          /mdysyymm/              ")
print("             /dmyssyydm/  sh       hh/     -hy  .dmyssyymm/              ")
print("              dmhssssydd/ -hdhysshdysdhssyhdd  -hmhyssyymd/              ")
print("              ymhssssyyddo``. //+/.` ./+// -` /ddhysssyhmh               ")
print("              +mdysssssyhdh `     `/+`      -sddysssssydmo               ")
print("               ymhysssssyyddh/`   `dm.   ` sddhysssssyhmh/               ")
print("               /hmhysssssyyyhdds ..dm . ohddhyyssssyyhmd+                ")
print("                /yddhyssssssyyhhddhddddddhyyssssssyydmh+                 ")
print("               /+sdmmdhhyyyysssyyyyyyyyyysssyyyyyhddmdyo+/               ")
print("           /+shdddhhyhhddddddhhhhhhhhhhhhhhdddddddhyyhhdddyo/            ")
print("         /shddhyyysssssyyyyhhhhhhhhhhhhhhhhhhyyyyyssssyyyhdddy+          ")
print("        /hmhyyssssssssssssssssssssssssssssssssssssssssssssyyhddo         ")
print("        /dmhyyyyyssssssssssssssssssssssssssssssssssssssyyyyyydms         ")
print("         +yhddddddhhhhhyyyyyyyyyyyyyyyyyyyyyyyyyyhhhhhdddddddhs/         ")
print("           //++oossyyhhhhhhhdddddddddddddddddhhhhhhyyssoo++///           ")
print("                       ///////+++++++++++++//////                        ")
print("                        ___  _                 ___   ____                ")
print("                       / _ \(_)               |  _ \|  __ \              ")
print("                 ____ | | | | |___   _   ____ | |_| | |__) |             ")
print("                |  _ \| | | | / __|/ _ \|  _ \| |_ <|  _  /              ")
print("                | |_) | |_| | \__ \ (_) | | | | |_| ) | \ \              ")
print("                |  __/ \___/|_|___/\___/|_| |_|____/|_|  \_\             ")
print("                | |*t.me/p0isonBR*                                       ")
print("                |_|*by p0isonBR*                                         ")

import time
time.sleep(5)
os.system('cls' if os.name == 'nt' else 'clear')


print("        ___  _                 ____  _____ ")
print("       / _ \(_)               |  _ \|  __ \ ")
print(" _ __ | | | |_ ___  ___  _ __ | |_) | |__) | ")
print("| '_ \| | | | / __|/ _ \| '_ \|  _ <|  _  / ")
print("| |_) | |_| | \__ \ (_) | | | | |_) | | \ \ ")
print("| .__/ \___/|_|___/\___/|_| |_|____/|_|  \_\ ")
print("| | SMS Sender 1.0")
print("|_| by p0isonBR")
print("    t.me/p0isonBR")
print(" ")

print("Sending SMS...")

url = "https://rest-api.d7networks.com/secure/send"
payload = {
  'from': '27700',
  'dlr': 'yes',
  'dlr-method': 'GET',
  'dlr-level': '2',
  'dlr-url': 'http://yourcustompostbackurl.com'
}

payload['username'] = input("Your API username: ")
payload['password'] = input("Your API password: ")
payload['to'] = input("Number destination: ")
payload['content'] = input("SMS content: ")

headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
}

import requests
response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
