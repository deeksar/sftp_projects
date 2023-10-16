
import pysftp
# SFTP credentials
SFTP_HOST = "Your_hostname"
SFTP_USER = "Your_username"
SFTP_PASSWORD = "Your_password"
SFTP_PORT = 22
SFTP_ROOT_FOLDER = "your_directory"

SFTP_PROCESS_FOLDER = "folder1"


def create_folders():
    try:

        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        with pysftp.Connection(
                host=SFTP_HOST,
                username=SFTP_USER,
                password=SFTP_PASSWORD,
                port=SFTP_PORT,
                cnopts=cnopts
        ) as srv:
            print("SFTP connection successful.")

            # List of folder names to create
            folders_to_create = [SFTP_PROCESS_FOLDER,]
            for folder in folders_to_create:
                folder_path = SFTP_ROOT_FOLDER + '/' + folder
                try:
                    srv.mkdir(folder_path)
                    print(f"Folder '{folder_path}' created successfully.")
                except Exception as e:
                    print(f"Failed to create folder '{folder_path}'. Error:", e)
    except Exception as e:
        print("Error:", e)

create_folders()
