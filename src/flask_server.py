import json
from time import sleep
from flask import Flask
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST,1)
s.bind(('', 50001))

try:
    while True:
        with open("/home/soxxz/projetos/code/ELITE-APP/src/Status.json") as jsonFile:
            jsonObject = json.load(jsonFile)
            jsonFile.close()
            print(jsonObject)
        sleep(0.5)
        s.sendto(bytes(str(jsonObject), encoding="utf-8"), ('<broadcast>', 50000))
except KeyboardInterrupt:
    print('interrupted!')


