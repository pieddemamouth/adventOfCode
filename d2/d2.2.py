#!/usr/bin/python

import sys
import re

if __name__ == "__main__":
    fo = open(sys.argv[1],"r")
    lines = fo.readlines()
    pos = [2,0]
    pad = [["X","X","1","X","X"],["X","2","3","4","X"],["5","6","7","8","9"],["X","A","B","C","X"],["X","X","D","X","X"]]

    for line in lines:
        #move = move.replace(" ","")
        line = line.strip()
        length = len(line)
        for step in range(length):
            if line[step] == "U":
                prev = pos[0]
                pos[0] = pos[0] - 1
                if pos[0] < 0:
                    pos[0] = 0
                if pad[pos[0]][pos[1]] == "X":
                    pos[0] = prev

            if line[step] == "D":
                prev = pos[0]
                pos[0] = pos[0] + 1
                if pos[0] > 4:
                    pos[0] = 4
                if pad[pos[0]][pos[1]] == "X":
                    pos[0] = prev

            if line[step] == "L":
                prev = pos[1]
                pos[1] = pos[1] - 1
                if pos[1] < 0:
                    pos[1] = 0
                if pad[pos[0]][pos[1]] == "X":
                    pos[1] = prev

            if line[step] == "R":
                prev = pos[1]
                pos[1] = pos[1] + 1
                if pos[1] > 4:
                    pos[1] = 4
                if pad[pos[0]][pos[1]] == "X":
                    pos[1] = prev

        print(pad[pos[0]][pos[1]])
#        print(orientations[orientation])
#        pos[0] = pos[0] + orientations[orientation][1] * length
#        pos[1] = pos[1] + orientations[orientation][2] * length
#        print(pos)
#    print(abs(pos[0]) + abs(pos[1]))
