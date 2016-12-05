#!/usr/bin/python

import sys
import re

if __name__ == "__main__":
    fo = open(sys.argv[1],"r")
    lines = fo.readlines()

    cpt = 0
    lineCpt = 0
    stack0 = []
    stack1 = []
    stack2 = []
    for line in lines:
        line = line.strip().split(" ")
        line = filter(None,line)
        line = map(int,line)
        
        stack0.append(line[0])
        stack1.append(line[1])
        stack2.append(line[2])

        lineCpt += 1

        if lineCpt == 3:

            if (stack0[0] + stack0[1]) > stack0[2] and (stack0[1] + stack0[2]) > stack0[0] and (stack0[0] + stack0[2]) > stack0[1]:
                print(str(stack0) + " :  ok")
                cpt += 1
            else:
                print(str(stack0) + " :  not ok")
            del stack0[:]

            if (stack1[0] + stack1[1]) > stack1[2] and (stack1[1] + stack1[2]) > stack1[0] and (stack1[0] + stack1[2]) > stack1[1]:
                print(str(stack1) + " :  ok")
                cpt += 1
            else:
                print(str(stack1) + " :  not ok")
            del stack1[:]

            if (stack2[0] + stack2[1]) > stack2[2] and (stack2[1] + stack2[2]) > stack2[0] and (stack2[0] + stack2[2]) > stack2[1]:
                print(str(stack2) + " :  ok")
                cpt += 1
            else:
                print(str(stack2) + " :  not ok")
            del stack2[:]

            lineCpt = 0

    print(cpt)
