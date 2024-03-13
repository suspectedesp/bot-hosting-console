import os

urls = [
    'https://bot-hosting.net/api/me'
]
try:
    import load_config as config
    auth = config.load('auth')
    clear = config.load('clear')
    
    import requests
    print(f"{auth}")
    if clear == "True":
        os.system('cls' if os.name == 'nt' else 'clear')
    print("Successfully Loaded data from config.json")
    print("Successfully imported requests")
    
except ModuleNotFoundError as e:
    module_name = str(e).split("'")[1]
    os.system(f"pip install {module_name}")
    os.system("python settings.account_settings.py")


def account(auth):
    print("""
1. Get Genuine Account Information
What do you want to do?""")
    match input("[>]"):
        case "1":
            headers = {"Authorization": f"{auth}"}
            response = requests.get(urls[0], headers=headers)
            if response.status_code == 200:
                print("Successfully visited /api/me")
                re = response.json()
                username = re.get('username')
                if username.endswith('#0'):
                    username = username[:-2]
                    print(username + ", it's nice to see you!")
                else:
                    print(username + ", it's nice to see you!")
                user_id = re.get('id')
                coins = re.get('coins')
                print(f"Your ID: {user_id}")
                print(f"Your Coins Amount: {coins}")
                
        case _:
            os.system('cls' if os.name == "nt" else 'clear')
            print("Invalid Input, Please Try again.")
            account(auth=auth)


account(auth=auth)


if __name__ == "__main__":
    print("Closing")
