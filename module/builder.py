from colorama import Fore, Back
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
                self.build_payload()
            elif user_input == "2": # Windows
                pass
            elif user_input == "3": # Back to menu
                pass
            elif user_input == "4": # exit
                exit("\n\nGood Luck!\n")

        except:
            exit("\n\nGood Luck!\n")
    
    def build_payload(self):
        self.get_payload_details()
        
        self.banner()

        payload_data = ""
        with open("payloads/generate.c", 'w') as f:
            f.write(payload_data)

        

        print(Fore.BLUE+" Your payload is running...")
        input(Fore.LIGHTRED_EX+" [*] Back to Menu (Press Enter...) "+self.reset)
    
    def get_payload_details(self):
        self.banner()
        
        print(Back.BLACK+"\n pick a name for your payload. > malware "+self.reset+"\n")
        payload_name =  input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"STORM-BREAKER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.CYAN+"/"+Fore.WHITE+"PAYLOAD"+Fore.CYAN+"/"+Fore.BLUE+"get payload name"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")

        print(Back.BLACK+"\n pick a PORT address for your payload. > malware "+self.reset+"\n")
        port_address =  input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"STORM-BREAKER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.CYAN+"/"+Fore.WHITE+"PAYLOAD"+Fore.CYAN+"/"+Fore.BLUE+"get payload name"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")

        print(Back.BLACK+"\n pick a IP address for your payload. > malware "+self.reset+"\n")
        ip_address =  input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"STORM-BREAKER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.CYAN+"/"+Fore.WHITE+"PAYLOAD"+Fore.CYAN+"/"+Fore.BLUE+"get payload name"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")

        self.payload_name = "malware" if payload_name == "" else payload_name
        self.port_address = "8080" if port_address == "" else port_address
        self.ip_address = "127.0.0.1" if ip_address == "" else ip_address
