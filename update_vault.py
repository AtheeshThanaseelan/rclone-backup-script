import rclone_lib
import sys

def help():
    print("--pull   \t\t\t Create folders and pull from cloud")
    print("--check  \t\t\t Check if folders are correctly synced to cloud")
    print("--push   \t\t\t Sync local folders with cloud")
    print("--setup  \t\t\t Setup folders, setup cloud, pull from cloud ")


def setup():
    rclone_lib.getRclone()
    rclone_lib.configureRemote("gdriveADF")

def pull():
    rclone_lib.pullRemote("gdriveADF", "Vault")

def push():
    rclone_lib.pushRemote("gdriveADF", "Vault")

def check():
    print("-------------------The following should not have errors -------------------")
    rclone_lib.pullRemote("gdriveADF", "Vault")


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