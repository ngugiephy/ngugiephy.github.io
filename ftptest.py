import ftplib
import os
 
def upload(ftp, file):
    ext = os.path.splitext(file)[1]
    if ext in (".txt", ".htm", ".html"):
        ftp.storlines("STOR " + file, open(file))
    else:
        ftp.storbinary("STOR " + file, open(file, "rb"), 1024)
 
try:
    ftp = ftplib.FTP("213.168.249.180")
    ftp.login("raspi", "raspberry")
    print "logged in to ftp"
except: 
    print "couldnt log in"
 
upload(ftp, "updater.py")