#!/usr/bin/python3

import hashlib

def representsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def checkValid(string):
    if string[0] == "0" and string[1] == "0" and string[2] == "0"  and string[3] == "0"  and string[4] == "0":
        return True
    else:
        return False

def makeHash(base,cpt):
    m = hashlib.md5()
    composed = base + str(cpt)
    m.update(composed.encode('utf-8'))
    hashed = m.hexdigest()
    return hashed

if __name__ == "__main__":
    #base = "abc"
    base = "ojvtpuvg"
    cpt = 0
    hashed = makeHash(base,cpt)
    
    completed = 0
    password = [" "] * 8

    while completed < 8:
        while checkValid(hashed) == False:
            cpt += 1
            hashed = makeHash(base,cpt)
        
        place = 0
        if representsInt(hashed[5]):
            place = int(hashed[5])
            val = hashed[6]

            if place < 8:
                if password[place] == " ":
                    password[place] = val
                    completed += 1
                    print("".join(password))

        cpt += 1
        hashed = makeHash(base,cpt)
