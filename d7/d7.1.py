#!/usr/bin/python3

import sys
import re
import heapq

def checkAbba(strings):
    oneStringOk = False
    for string in strings:
        thisStringOk = True
        for idL in range(len(string)-4):
            if string[idL] != string[idL+1] and string[idL] == string[idL+3] and string[idL+1] == string[idL+2]:
            

if __name__ == "__main__":
    fo = open(sys.argv[1],"r")
    lines = fo.readlines()

    for line in lines:
        line = line.strip()
        print(line)
        #get the hypernets
        hypernets = re.findall("\[([a-z]+)\]",line)
        print(hypernets)
        #get the rest
        strings = re.sub(r"\[[a-z]+\]",".",line).split(".")
        print(strings)

