from colorama import Fore, Style, Back
import os, platform, subprocess

from module.menu import Menu


class Main:
    def __init__(self):
        self.menu = Menu()
        self.start_app()
    
    def get_input(self):
        try:
            return input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"STORM-BREAKER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")
        except:
            exit("\n\nGood luck!\n")

    def start_app(self):
        while True:
            self.menu.show_menu()
            user_input = self.get_input()
            print(user_input)

Main()
