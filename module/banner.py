from colorama import Fore, Style, Back
from time import sleep


class Menu:
    def __init__(self):
        self.show_menu()
        
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

        """+Style.RESET_ALL)

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
        print(Fore.RED+"[4]"+Fore.WHITE+" Exit ... \n")

    def show_menu(self):
        self.banner()
        self.infolist()