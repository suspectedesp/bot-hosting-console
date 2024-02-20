import json
import os

def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_function
def load():
    if not os.path.exists('config.json'):
        print("Config file not found. Creating...")
        create_config()
        load()
    try:
        with open('config.json') as config:
            data = json.load(config)
            auth = data.get('auth')
            if auth is None:
                return json.load(config)
            elif auth is not None:
                return auth
    except json.decoder.JSONDecodeError:
        print("Error: Invalid JSON format in config.json. Deleting and recreating the file...")
        os.remove('config.json')
        create_config()

@log_function
def create_config():
    auth = input("Config file created. Please provide authorization.")
    data = {'auth': auth}
    with open('config.json', 'w') as config:
        json.dump(data, config)


if __name__ == '__main__':
    print("Closing")
