#!/usr/bin/python3

import sys
import re
import heapq

if __name__ == "__main__":
    fo = open(sys.argv[1],"r")
    lines = fo.readlines()

    sumSectors = 0
    for line in lines:
        line = line.strip().split("-")
        print(line)
        counts = [0] * 26
        for block in line[:-1]:
            for letter in block:
                counts[ord(letter)-ord("a")] += 1

        largest = [0] * 5
        largestIndex = [-1] * 5
        for idC,letterCount in enumerate(counts):
            val = min(largest)
            idL = largest.index(val)
            if letterCount > val:
                largest[idL] = letterCount
                largestIndex[idL] = idC
        pattern = re.compile("([0-9]+)\[([a-z]+)\]")
        m = pattern.match(line[-1])
        sectorId = int(m.group(1))

        fail = False
        for letter in m.group(2):
            if not (ord(letter)-ord("a") in largestIndex or counts[ord(letter)-ord("a")] == min(largest)):
                fail = True
                break

        if fail == False:
            sumSectors += sectorId

    print(sumSectors)
