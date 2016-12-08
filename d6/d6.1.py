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
        letter = distLetter.index(max(distLetter))
        sys.stdout.write(chr(letter + ord("a")))
