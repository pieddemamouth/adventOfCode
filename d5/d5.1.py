#!/usr/bin/python3

import hashlib

def checkValid(string):
    if string[0] == "0" and string[1] == "0" and string[2] == "0"  and string[3] == "0"  and string[4] == "0":
        return True
    else:
        return False

if __name__ == "__main__":
    base = "ojvtpuvg"
    cpt = 0
    m = hashlib.md5()
    composed = base + str(cpt)
    m.update(composed.encode('utf-8'))
    hashed = m.hexdigest()
    
    for i in range (8):
        while checkValid(hashed) == False:
            cpt += 1
            m = hashlib.md5()
            composed = base + str(cpt)
            m.update(composed.encode('utf-8'))
            hashed = m.hexdigest()
            #print(str(cpt) + ": " + str(hashed))
        
        print(hashed[5])
        cpt += 1
        m = hashlib.md5()
        composed = base + str(cpt)
        m.update(composed.encode('utf-8'))
        hashed = m.hexdigest()
