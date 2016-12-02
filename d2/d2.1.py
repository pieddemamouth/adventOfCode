#!/usr/bin/python

import sys
import re

if __name__ == "__main__":
    fo = open(sys.argv[1],"r")
    lines = fo.readlines()
    pos = [1,1]
    pad = [[1,2,3],[4,5,6],[7,8,9]]

    for line in lines:
        #move = move.replace(" ","")
        line = line.strip()
        length = len(line)
        for step in range(length):
            if line[step] == "U":
                pos[0] = pos[0] - 1
                if pos[0] < 0:
                    pos[0] = 0
            if line[step] == "D":
                pos[0] = pos[0] + 1
                if pos[0] > 2:
                    pos[0] = 2
            if line[step] == "L":
                pos[1] = pos[1] - 1
                if pos[1] < 0:
                    pos[1] = 0
            if line[step] == "R":
                pos[1] = pos[1] + 1
                if pos[1] > 2:
                    pos[1] = 2
        print(pad[pos[0]][pos[1]])
#        print(orientations[orientation])
#        pos[0] = pos[0] + orientations[orientation][1] * length
#        pos[1] = pos[1] + orientations[orientation][2] * length
#        print(pos)
#    print(abs(pos[0]) + abs(pos[1]))
