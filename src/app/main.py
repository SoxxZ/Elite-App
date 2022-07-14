from socket import *
import sys
import json
from time import sleep

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.clock import Clock

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 50000))

response, ip = s.recvfrom(1024)
response = response.decode("utf-8")
response = response.replace("\'", "\"")
print(response)
print(type(response))

jsonObject = json.loads(response)

print(jsonObject)

print(type(jsonObject))

flags_desc = [
"srvHighBeam",
"fsdJump",
"Altitude from Average radius",
"Night Vision",
"Hud in Analysis mode",
"In SRV",
"In Fighter",
"In MainShip",
"Being Interdicted",
"IsInDanger",
"Has Lat Long",
"Over Heating ( > % )",
"Low Fuel ( < % )",
"Fsd Cooldown",
"Fsd Charging",
"Fsd MassLocked",
"Srv DriveAssist",
"Srv Turret retracted (close to ship)",
"Srv using Turret view",
"Srv Handbrake",
"Scooping Fuel",
"Silent Running",
"Cargo Scoop Deployed",
"LightsOn",
"In Wing",
"Hardpoints Deployed",
"FlightAssist Off",
"Supercruise",
"Shields Up",
"Landing Gear Down",
"Landed (on planet surface)",
"Docked (on a landing pad)"
]

flags = jsonObject['Flags']
pips = jsonObject['Pips']
firegroup = jsonObject['FireGroup']
gui_focus = jsonObject['GuiFocus']
fuel_main = jsonObject['Fuel']["FuelMain"]
fuel_reservoir = jsonObject['Fuel']['FuelReservoir']

flags_bin = list('{0:#034b}'.format(flags))
flags_bin = flags_bin[2:34:1]

def update_values():
    response, ip = s.recvfrom(1024)
    response = response.decode("utf-8")
    response = response.replace("\'", "\"")
    print(response)
    print(type(response))

    jsonObject = json.loads(response)

    print(jsonObject)
    print(type(jsonObject))

    flags = jsonObject['Flags']
    pips = jsonObject['Pips']
    firegroup = jsonObject['FireGroup']
    gui_focus = jsonObject['GuiFocus']
    fuel_main = jsonObject['Fuel']["FuelMain"]
    fuel_reservoir = jsonObject['Fuel']['FuelReservoir']
    flags_bin = list('{0:#034b}'.format(flags))
    flags_bin = flags_bin[2:34:1]
    return pips, firegroup, gui_focus, fuel_main, fuel_reservoir, flags_bin

class MainApp(MDApp):
    title = "Elite App"
    def build(self):
        self.theme_cls.theme_style = "Dark"
        Clock.schedule_once(self.update, 0.5)
        return Builder.load_file('design.kv')

    def update(self, *args):
        pips, firegroup, gui_focus, fuel_main, fuel_reservoir, flags_bin = update_values()
        i = 0
        x = 0
        while i < len(flags_desc):
            x = "self.root.ids."+"item"+str(i+1)
            x = eval(x)
            x.text = flags_desc[i]
            x.secondary_text = flags_bin[i]
            i = i+1
        i = 0
        while i < len(pips):
            p = "self.root.ids."+"pip"+str(i+1)
            p = eval(p)
            p.secondary_text = str(pips[i])
            i = i+1
            
        
        Clock.schedule_once(self.update, 0.5)

MainApp().run()