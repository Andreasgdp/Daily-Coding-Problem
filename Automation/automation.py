import sys
import os

path = os.path.join(os.environ['USERPROFILE'], "GitHub/Daily-Coding-Problem/")

def create():
    folderName = str(sys.argv[1])
    newPath = path + folderName
    os.mkdir(newPath)


if __name__ == "__main__":
    create()
