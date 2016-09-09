#!/usr/bin/env python3
import subprocess
import os
import sys

global AIName
AIName = ""

def Usrin():
    global UsrInput
    UsrInput = input("Whats your command Sir ? :")
    return UsrInput


def splashscreen():

    with open('splash.txt') as splash:
        for line in splash:
            line = line.strip("/n")
            print(line, end = "")
    return;


def readcommands():

    with open('commands.txt') as Commandf:
       for line in Commandf:
           spli = line.split("|")
           #print(spli)
           if line.startswith("#"):
               next
           elif UsrInput == spli[0]:
               print(spli[1])
               print(" ")
               #print("I know this Word")
               if spli[2] == "1":
                   #print("I know this command")
                   os.system(spli[3])
                   print(" ")
                   break
           else:
               next
    return;
#subprocess.call("cat ~/github/py-yar/splash.txt")


splashscreen()


while True:
    Usrin()
    readcommands()
