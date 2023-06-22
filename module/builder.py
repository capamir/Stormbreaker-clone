from colorama import Fore
import subprocess, platform

from .menu import Menu

class Builder(Menu):
    def __init__(self):
        self.select_payload()
    
    def select_payload(self):
        self.show_builder_menu()
        try:
            user_input =  input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"STORM-BREAKER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.CYAN+"/"+Fore.BLUE+"Payload"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")
            
            if user_input == "1": # C Payload
                self.select_platform()

            elif user_input == "2": # Back to menu
                pass
            elif user_input == "3": # exit
                exit("\n\nGood Luck!\n")

        except:
            exit("\n\nGood Luck!\n")
    
    def select_platform(self):
        self.show_platform_menu()
        try:
            user_input =  input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"STORM-BREAKER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.CYAN+"/"+Fore.BLUE+"Select Platform"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")
            
            if user_input == "1": # Linux
                pass
            elif user_input == "2": # Windows
                pass
            elif user_input == "3": # Back to menu
                pass
            elif user_input == "4": # exit
                exit("\n\nGood Luck!\n")

        except:
            exit("\n\nGood Luck!\n")
    