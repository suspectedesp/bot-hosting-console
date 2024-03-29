import os

url = [
    'https://bot-hosting.net/api/servers',
    'https://bot-hosting.net/api/manageservers'
]


try:
    from load_config import load
    auth = load(str="auth")
    
    import requests
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Successfully Loaded data from config.json")
    print("Successfully imported requests")
    
except ModuleNotFoundError as e:
    module_name = str(e).split("'")[1]
    if module_name == "load_config":
        input(f"Make sure you did not delete any files, for example {module_name}")
    else:
        os.system(f"pip install {module_name}")
    os.system("python settings.server_settings.py" if os.name=="nt"
              else "python3 settings.server_settings.py")


def server(auth):
    headers = {"Authorization": f"{auth}"}
    print("""
1. Get Genuine Server Information
2. Manage a certain Server
What do you want to do?""")
    match input("[>]"):

        case "1":
            response = requests.get(url[0], headers=headers)
            if response.status_code == 200:
                print("Successfully visited /api/servers")
                re = response.json()
                print(re)
                
        case _:
            os.system('cls' if os.name == "nt" else 'clear')
            print("Invalid Input, Please Try again.")
            server(auth=auth)


server(auth=auth)

if __name__ == "__main__":
    print("Closing")
