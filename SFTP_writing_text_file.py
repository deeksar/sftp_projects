#  Import pysftp library 
import pysftp

#giving your credentials
SFTP_HOST = "Your_hostname"
SFTP_USER = "Your_username"
SFTP_PASSWORD = "Your_password"
SFTP_PORT = 22
SFTP_ROOT_FOLDER = "your_folder_path"

# function to connect and process
def func():
    #Connection Options Object : cnopts
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys= None
    with pysftp.Connection(host=SFTP_HOST, username= SFTP_USER, password= SFTP_PASSWORD, port=SFTP_PORT, cnopts= cnopts):
        print("connected!!!")
        with open("new.txt","w") as text:
            text.write("hello this is the text file!")


func()
