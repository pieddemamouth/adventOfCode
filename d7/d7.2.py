#!/usr/bin/python3

import sys
import re
import heapq

def checkBaB(AbAs,strings):
    resCheck = True
    for local in AbAs:
        resAba = False
        for aba in local:
            bab = aba[1] + aba[0] + aba[1] 
            for string in strings:
                if bab in string:
                    resAba = True 
                    break
            if resAba == True:
                break
        if resAba == False:
            resCheck = False
            break
    return resCheck


def findAbA(strings):
    abas = []
    for string in strings:
        local = []
        for idL in range(len(string)-2):
            if string[idL] != string[idL+1] and string[idL] == string[idL+2]:
                local.append(string[idL:idL+3])
        if len(local) > 0:
            abas.append(local)
    return abas

if __name__ == "__main__":
    fo = open(sys.argv[1],"r")
    lines = fo.readlines()

    cpt = 0
    for line in lines:
        line = line.strip()
        #get the hypernets
        hypernets = re.findall("\[([a-z]+)\]",line)
        #get the rest
        strings = re.sub(r"\[[a-z]+\]",".",line).split(".")
        abas = findAbA(strings)
        if len(abas) > 0:
            if checkBaB(abas,hypernets) == True:
                cpt += 1
            else:
                print("does not support")
                print(line)
                print(abas)
    print(cpt)
