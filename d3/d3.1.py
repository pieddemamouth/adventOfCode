#!/usr/bin/python

import sys
import re

if __name__ == "__main__":
    fo = open(sys.argv[1],"r")
    lines = fo.readlines()

    cpt = 0
    for line in lines:
        line = line.strip().split(" ")
        line = filter(None,line)
        line = map(int,line)
        if (line[0] + line[1]) > line[2] and (line[1] + line[2]) > line[0] and (line[0] + line[2]) > line[1]:
            print(str(line) + " :  ok")
            cpt += 1
        else:
            print(str(line) + " :  not ok")
    print(cpt)
