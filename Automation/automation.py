import sys
import os

path = "C:/Users/andre/GitHub/Daily-Coding-Problem/"


def create():
    folderName = str(sys.argv[1])
    newPath = str(path) + str(folderName)
    os.mkdir(newPath)


if __name__ == "__main__":
    create()
