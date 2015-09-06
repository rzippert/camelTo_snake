#!/bin/python
###############################################################
# Python script that converts camel case expressions to snake #
# case expressions. Useful for coding but doesn't smartly     #
# ignore anything. You are supposed to check all this script  #
# does.                                                       #
###############################################################

import sys #used to read arguments
import os #used to test for files and dirs 

def fileRead (filePath) :
    textfile = open(filePath,"r")
    print("Reading "+ filePath+"...")
    text = textfile.read()
    textfile.close()
    #iteration through text
    for i in range( 0, text.rfind( text[-1] ) ) : #iterate the whole string
        if text[i].islower() : #if a lowercase letter is found
            x = i+1 #gets the next index
            while text[x].islower() : x = x+1 #tests next letters until one is not lowercase
            if text[x].isupper() : #if this non lowercase is uppercase
                text = text[1:x] + "_" + text[x].lower() + text[x+1:] #copies string replacing the uppercase with _ and lowercase
    textfile = open(filePath,"w") #writes the result back over the file
    textfile.write(text)
    textfile.close()

def directoryRead (folderpath) :
    for files in os.listdir(folderpath) : #iterates over the folder contents
        if os.path.isfile(files) :
            fileRead(files) #Convert the file
        elif os.path.isdir(files) :
            directoryRead(files) #Lists this folder recursively

if len(sys.argv) < 2 :
    print("I won't guess what file you want me to read dumbass...")
    sys.exit(-1)
    
#Reading the argument as a file or directory
for i in range(1,len(sys.argv)) :
    if os.path.isdir(sys.argv[i]) :
        print("You told me to write over everything on " + sys.argv[i] + ". I hope you know what you're doing, because I don't...")
        directoryRead(sys.argv[i]) #Get all files inside the folder and then read and write over them
    elif os.path.isfile(sys.argv[i]) :
        fileRead(sys.argv[i]) #Read and write on file directly

print("Don't forget to check what I've done. Your code isn't working anymore./nYou're welcome :)")
sys.exit(0) #Program ran correctly (I guess)
