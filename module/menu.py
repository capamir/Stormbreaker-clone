from colorama import Fore, Style, Back
from time import sleep
import os, platform

class Menu:
    reset = Style.RESET_ALL
    def __init__(self):
        # self.show_menu()
        pass
        
    def banner(self):
        print(Fore.RED+"""
$$\   $$\  $$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$\  
$$ |  $$ |$$  __$$\ $$  __$$\ $$ | $$  |$$  _____|$$  __$$\ 
$$ |  $$ |$$ /  $$ |$$ /  \__|$$ |$$  / $$ |      $$ |  $$ |
$$$$$$$$ |$$$$$$$$ |$$ |      $$$$$  /  $$$$$\    $$$$$$$  |
$$  __$$ |$$  __$$ |$$ |      $$  $$<   $$  __|   $$  __$$< 
$$ |  $$ |$$ |  $$ |$$ |  $$\ $$ |\$$\  $$ |      $$ |  $$ |
$$ |  $$ |$$ |  $$ |\$$$$$$  |$$ | \$$\ $$$$$$$$\ $$ |  $$ |
\__|  \__|\__|  \__| \______/ \__|  \__|\________|\__|  \__|

        """+self.reset)

    def infolist(self):
        sleep(0.1)
        print(Fore.RED+" ["+Fore.WHITE+"*"+Fore.RED+"]"+Fore.CYAN+" Choose one of the options below. \n")
        sleep(0.1)
        print(Fore.RED+"[1]"+Fore.WHITE+" Build Payload \n")
        sleep(0.1)
        print(Fore.RED+"[2]"+Fore.WHITE+" Start Listener \n")
        sleep(0.1)
        print(Fore.RED+"[3]"+Fore.WHITE+" Settings \n")
        sleep(0.1)
        print(Fore.RED+"[4]"+Fore.WHITE+" Exit ... \n"+self.reset)

    
    def clear(self):
        osname = platform.uname()[0]
        if osname == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def show_menu(self):
        self.clear()
        self.banner()
        self.infolist()
    