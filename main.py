import os
import subprocess

class File:
    isDir = False
    name = ''

fileList = []

def appendToFileList(currentDirectory):
    currentDirectory = currentDirectory.decode('UTF-8')

    temp = File()
    for i in range (len(currentDirectory)):
        if currentDirectory[i] == '\n':
            
            if isdir(temp.name):
                temp.isDir = True
            

            fileList.append(temp)
            temp = File()
        else:
            temp.name += currentDirectory[i]



os.chdir('/')

currentDirectory = subprocess.check_output('ls')

appendToFileList(currentDirectory)


