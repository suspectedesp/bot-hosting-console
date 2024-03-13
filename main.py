import os
import subprocess

try:
    import colorama
    from colorama import Fore
    from settings.load_config import create_config
    colorama.init(convert=True)
    
except ModuleNotFoundError as module_not_found:
    module_name = str(module_not_found).split("'")[1]
    os.system(f"pip install {module_name}")
    os.system("cls" if os.name=="nt" else "clear")
    os.system("python main.py")


def menu():
    try:
        username = subprocess.check_output("whoami", shell=True, text=True).strip()
        print(Fore.BLUE + """
 ____  _   _        ____                      _      
| __ )| | | |      / ___|___  _ __  ___  ___ | | ___ 
|  _ \| |_| |_____| |   / _ \| '_ \/ __|/ _ \| |/ _ \\
| |_) |  _  |_____| |__| (_) | | | \__ \ (_) | |  __/
|____/|_| |_|      \____\___/|_| |_|___/\___/|_|\___|
        """)
        print("Welcome, " + username)
        print("""
1. Account Settings
2. Server Settings
3. Actualise config.json
What do you want to do today?""")
        match input("[>]"):
            case "1":
                os.system('cls' if os.name == "nt" else 'clear')
                os.system("py ./settings/account_settings.py")
                
            case "2":
                os.system('cls' if os.name == "nt" else 'clear')
                os.system("py ./settings/server_settings.py")
                
            case "3":
                os.system('cls' if os.name == "nt" else 'clear')
                create_config("menu")
                
            case _:
                input("Invalid Input, press enter to retry")
                os.system('cls' if os.name == "nt" else 'clear')
                menu()
                
    except subprocess.CalledProcessError as process_error:
        print(f"Failed to fetch username, error: {process_error}")
        input("Press enter to close")


if __name__ == "__main__":
    menu()
