#!/usr/bin/python3

import sys
import re
import heapq

if __name__ == "__main__":
    fo = open(sys.argv[1],"r")
    lines = fo.readlines()

    distribution = []
    for i in range(8):
        distribution.append([0] * 26)

    for line in lines:
        line = line.strip()
        for letter in range(len(line)):
            distribution[letter][ord(line[letter])-ord("a")] += 1

    for distLetter in distribution:
        minId = 0
        minVal = 200
        for check in range(len(distLetter)):
            if distLetter[check] < minVal and distLetter[check] != 0:
                minVal = distLetter[check]
                minId = check
        #letter = distLetter.index(min(distLetter))
        sys.stdout.write(chr(minId + ord("a")))
    print("")
