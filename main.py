from colorama import Fore, Style, Back
import os, platform, subprocess

from module.menu import Menu
from module.builder import Builder
from time import sleep


class Main(Menu):
    def __init__(self):
        self.start_app()
    
    def get_input(self):
        try:
            user_input =  input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"STORM-BREAKER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")
            
            if user_input == "1": # payload
                Builder()
            elif user_input == "2":
                pass
            elif user_input == "3": # settings
                pass
            elif user_input == "4": # exit
                exit("\n\nGood Luck!\n")

        except:
            exit("\n\nGood Luck!\n")


    def start_app(self):
        while True:
            self.show_menu()
            self.get_input()


Main()
