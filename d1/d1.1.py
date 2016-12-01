#!/usr/bin/python

import sys
import re

if __name__ == "__main__":
    fo = open(sys.argv[1],"r")
    line = fo.readline()
    moves = re.split(",",line)
    pos = [0,0]
    orientation = 0
    orientations = [("N",0,1),("E",1,0),("S",0,-1),("O",-1,0)]
    for move in moves:
        move = move.replace(" ","")
        direction = ""
        length = 0
        #if len(move) == 2:
        print(move[0] + "." + move[1:])
        direction = move[0]
        length = int(move[1:])
        #if len(move) == 3:
        #    print(move[1] + "." + move[2:])
        #    direction = move[1]
        #    length = int(move[2:])
        if direction == "L":
            orientation = (orientation + 1) % 4
        if direction == "R":
            orientation = (orientation - 1) % 4
        print(orientations[orientation])
        pos[0] = pos[0] + orientations[orientation][1] * length
        pos[1] = pos[1] + orientations[orientation][2] * length
        print(pos)
    print(abs(pos[0]) + abs(pos[1]))
