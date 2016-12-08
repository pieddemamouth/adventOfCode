#!/usr/bin/python3

import sys
import re
import heapq

def checkAbba(strings):
    oneStringOk = False
    for string in strings:
        thisStringOk = False
        for idL in range(len(string)-3):
            if string[idL] != string[idL+1] and string[idL] == string[idL+3] and string[idL+1] == string[idL+2]:
                thisStringOk = True
                break
        if thisStringOk == True:
            oneStringOk = True
            break
    return oneStringOk

if __name__ == "__main__":
    fo = open(sys.argv[1],"r")
    lines = fo.readlines()

    cpt = 0
    for line in lines:
        line = line.strip()
        print(line)
        #get the hypernets
        hypernets = re.findall("\[([a-z]+)\]",line)
        #get the rest
        strings = re.sub(r"\[[a-z]+\]",".",line).split(".")
        if checkAbba(hypernets)  == False and checkAbba(strings) == True:
            print ("valid")
            cpt += 1
    print(cpt)
