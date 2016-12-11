#!/usr/bin/python

import sys
import re
import copy

def decompressOne(lines):
    decompression = False
    output = ""
    nbTags = 0
    for line in lines:
        mode = "normal"
        record = ""
        recordLength = -1
        tmpLength = ""
        nbRepeat = -1
        tmpRepeat = ""

        for char in line:
            if ord(char) != 10:
                if mode == "normal":
                    if char != "(" :
                        output = output + char
                    elif char == "(":
                        mode = "readTag"

                elif mode == "readTag":
                    decompression = True
                    nbTags += 1
                    if char == "x":
                        recordLength = int(tmpLength)
                        tmpLength = ""
                    elif char == ")":
                        nbRepeat = int(tmpRepeat)
                        tmpRepeat = ""
                        mode = "record"
                    elif recordLength == -1:
                        tmpLength = tmpLength + char
                    else:
                        tmpRepeat = tmpRepeat + char

                elif mode == "record":
                    if recordLength > 0:
                        record = record + char
                        recordLength -= 1
                        if recordLength == 0:
                            for i in range(nbRepeat):
                                output = output + record
                            record = ""
                            recordLength = -1
                            mode = "normal"

                else:
                    raise("unknown mode")

    print("nbTags: " + str(nbTags))
    return(decompression,output)

if __name__ == "__main__":
    fo = open(sys.argv[1],"r")
    lines = fo.readlines()

    decompression = True
    while decompression == True:
        decompression,lines = decompressOne(lines)
        print(len(lines))
        lines = [lines]
        #print(lines)

    print(len(lines[0]))
