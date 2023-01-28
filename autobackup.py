import os
import sys
import pathlib

FOLDERS = [pathlib.Path("D:\Documents\temp\_Vault")]

def makeFolders():
    for name in FOLDERS:
        #Check if folder exists
        if (not os.path.isdir(name)):
            print("INFO: Directory "+name+" not found, creating")
            os.system("mkdir "+name)
        else:
            print("INFO: Directory "+name+" found")

#Google Drive
def configGDrive2():
    createCommand = "rclone config create GDriveBase drive"
    os.system(createCommand)  

def fetchGDrive2(quietSync):
    for name in FOLDERS:
        if(quietSync):
            firstSyncCommand = "rclone sync --tpslimit 10 GDriveBase:Backup/"+name+" ./"+name
            os.system(firstSyncCommand)       
        else:
            firstSyncCommand = "rclone sync -vv --tpslimit 10 onedriveA10:Backups/"+name+" ./"+name
            os.system(firstSyncCommand)       

def syncGDrive2():
    for name in FOLDERS:
        firstSyncCommand = "rclone sync -i --tpslimit 10 ./"+name+" GDriveBase:Backup/"+name
        os.system(firstSyncCommand)           


#OneDrive
def configOneDrive():
    createCommand = "rclone config create onedriveA10"+" onedrive"
    os.system(createCommand)

def fetchOneDrive():
    for name in FOLDERS:
        firstSyncCommand = "rclone sync -vv --tpslimit 10 onedriveA10:Backups/"+name+" ./"+name
        os.system(firstSyncCommand)        

def syncOneDrive():
    for name in FOLDERS:
        firstSyncCommand = "rclone sync -i --tpslimit 10 ./"+name+" onedriveA10:Backups/"+name
        os.system(firstSyncCommand)           

#Once
    #'rclone listremotes'
    #check for backup1 (gdrive) and backup2 (onedrive/droopboox)
    #Make Folders
    #Make configs

#Repeat
    #Sync to drive


#Functional Functions
def help():
    print("--pull   \t\t\t Create folders and pull from cloud")
    print("--check  \t\t\t Check if folders are correctly synced to cloud")
    print("--push   \t\t\t Sync local folders with cloud")
    print("--setup  \t\t\t Setup folders, setup cloud, pull from cloud ")


def pull():
    fetchGDrive2(True)
    print("-------------------The following should not have errors -------------------")
    fetchOneDrive()

def push():
    syncGDrive2()
    syncOneDrive()

def check():
    print("-------------------The following should not have errors -------------------")
    fetchGDrive2(False)
    fetchOneDrive()


def setup():
    makeFolders()
    configGDrive2()
    configOneDrive()
    pull()


if __name__ == "__main__" :
    argc = len(sys.argv)
    if(argc > 1):
        arg1 = sys.argv[1]
        if(arg1 == "--setup"):
            setup()
        if(arg1 == "--push"):
            push()
        if(arg1 == "--pull"):
            pull()
        if(arg1 == "--check"):
            check()
    else:
        help()