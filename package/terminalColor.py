from colorama import Fore, Back, Style

def Yellow(text:str)->str:
    return Fore.YELLOW+text+Style.RESET_ALL

def Red(text:str)->str:
    return Fore.RED+text+Style.RESET_ALL

def Green(text:str)->str:
    return Fore.GREEN+text+Style.RESET_ALL

def Cyan(text:str)->str:
    return Fore.CYAN+text+Style.RESET_ALL

def Blue(text:str)->str:
    return Fore.BLUE+text+Style.RESET_ALL
