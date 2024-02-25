import os
import subprocess
import sys

sys.setrecursionlimit(100000) # Base 1000 limit might not be enough for deep recursion

wantedFile = '.minecraft' # Example file 

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

def skipNonFiles(file):
    firstTwoLetters = ''
    firstTwoLetters += file[0]
    
    if len(file) < 2 and file[0] == '.':
        return False
    if len(file) >= 2 and file[1] == '.':
        return False
    return True

def traverseDirectory(directory):
    os.chdir(directory)
    
    directory = subprocess.check_output(['ls', '-a'])
    directory = refactorDirectory(directory)
    
    for i in range (len(directory)):
        if (not(skipNonFiles(directory[i]))):
            continue
        if directory[i] == wantedFile:
            printCurrentDirectory()
            return True

        if os.path.isdir(directory[i]):
            traverseDirectory(directory[i])

    os.chdir('..')
    return

traverseDirectory('/home')
