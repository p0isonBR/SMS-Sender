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

import urllib.parse

USER = input("Your API username: ")
PASS = input("Your API password: ")
NUMBER = input("Destination number, with country code: ") 
SENDER = input("Custom sender number: ")
TEXT = input("SMS content: ")

print("Sending SMS...")

urllib.parse.quote(TEXT)

url = "https://http-api.d7networks.com/send"
querystring = {
"username":"USER",
"password":"PASS",
"from":"SENDER",
"content":"TEXT",
"dlr-method":"POST",
"dlr-url":"https://4ba60af1.ngrok.io/receive",
"dlr":"yes",
"dlr-level":"3",
"to":"NUMBER"
}
headers = {
'cache-control': "no-cache"
}
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
