import json
import os


def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        with open('config.json') as config:
            data = json.load(config)
            censor = data.get('censor')
            if censor:
                result = "[Censored]"
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper


@log_function
def load(str):
    if not os.path.exists('config.json'):
        print("Config file not found. Creating...")
        create_config()
        return None  # Returning None if config file doesn't exist
    try:
        with open('config.json') as config:
            data = json.load(config)
            auth = data.get('auth')
            censor = data.get('censor')
            clear = data.get('clear')
            if auth is None or censor is None or clear is None:
                create_config()
                return None
            else:
                if str == "auth":
                    return auth
                elif str == "clear":
                    return clear
    except json.decoder.JSONDecodeError:
        print("Error: Invalid JSON format in config.json. Deleting and recreating the file...")
        os.remove('config.json')
        create_config()


@log_function
def create_config():
    if os.path.exists('config.json'):
        os.remove('config.json')
    auth = input("Config file created. Please provide authorization: ")
    censor_input = input("Do you want it to censor or not? (True/False): ")
    if censor_input.lower() == "true":
        censor = True
    else:
        censor = False

    clear_input = input("Do you want it to clear or not? (True/False): ")
    if clear_input.lower() == "true":
        clear = "True"
    else:
        clear = "False"

    data = {'clear': clear, 'auth': auth, 'censor': censor}
    with open('config.json', 'w') as config:
        json.dump(data, config)


if __name__ == '__main__':
    print("Closing")
