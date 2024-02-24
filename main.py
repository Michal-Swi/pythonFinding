import os

import subprocess

wantedFile = 'lpr'

def refactorDirectory(currentDirectory):
    currentDirectory = currentDirectory.decode('UTF-8') 
    
    fileList = []

    temp = ''
    for i in range (len(currentDirectory)):
        if currentDirectory[i] == '\n': 
            fileList.append(temp)
            temp = ''
        else:
            temp += currentDirectory[i]

    return fileList

def printCurrentDirectory():
    currentDirectory = subprocess.check_output('pwd')
    currentDirectory = currentDirectory.decode('UTF-8').strip()
    currentDirectory += '/' + wantedFile

    print(currentDirectory)

def traverseDirectory(directory):
    os.chdir(directory)

    directory = subprocess.check_output('ls')
    directory = refactorDirectory(directory)

    for i in range (len(directory)):
        if directory[i] == wantedFile:
            printCurrentDirectory()
            return True

        if os.path.isdir(directory[i]): 
            traverseDirectory(directory[i])

    os.chdir('..')
    return

traverseDirectory('/')
