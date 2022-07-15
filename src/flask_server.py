import json
from sys import setswitchinterval
from time import sleep
from flask import Flask
from socket import *

from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST,1)
s.bind(('', 50001))

Builder.load_file('/home/soxxz/projetos/code/ELITE-APP/src/app/flask_design.kv')



class MyLayout(Widget):
    
    def switch_click(self, switchObject, switchValue):
        global switchState
        switchState = False
        print(type(switchValue))
        if(switchValue == True):
            switchState = switchValue
            Clock.schedule_interval(self.update, 0.5)
        else:
            Clock.unschedule(self.update)

    def process(self, text):
        global fdirectory
        fdirectory = text

    def update(self, *args):
        print(switchState)
        if switchState == True:
            with open(fdirectory) as jsonFile:
                jsonObject = json.load(jsonFile)
                jsonFile.close()
                print(jsonObject)
            sleep(0.5)
            s.sendto(bytes(str(jsonObject), encoding="utf-8"), ('<broadcast>', 50000))
                
print('a')
class MainApp(MDApp):
    title = "Elite App"
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return MyLayout()
    



MainApp().run()

