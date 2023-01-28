import os
from autobackup import *

'''

'''

#Dict: remote name : remote type
REMOTES = {
    "gdriveADF" : "drive",
    "onedriveA10" : "onedrive",

}


#Dict: onlinepath : localpath
FOLDERS = {
    "Vault" : str(pathlib.Path("E:\\Mine\\_Vault").resolve()),
}

def getRclone():
    url = r'https://downloads.rclone.org/rclone-current-windows-amd64.zip'
    print(f"Get RCLONE from {url}")
    print(f"Place rclone.exe beside rclone_lib.py")
    input(f"Press space when finished")

def configureRemote(remote_name):
    config_command = "rclone config create "+remote_name+" "+REMOTES[remote_name]
    os.system(config_command)  

def pushRemote(remote_name, folder_name):
    folder_path = FOLDERS[folder_name]
    push_command = "rclone sync -vv --tpslimit 10 "+folder_path+" "+remote_name+":"+folder_name+"/"
    os.system(push_command)  

def pullRemote(remote_name, folder_name, quiet=True):
    folder_path = FOLDERS[folder_name]
    if quiet == True:
        pull_command = "rclone sync --tpslimit 10 "+remote_name+":"+folder_name+"/" + " " + folder_path
    else:
        pull_command = "rclone sync -vv --tpslimit 10 "+remote_name+":"+folder_name+"/" + " " + folder_path
    os.system(pull_command)  

