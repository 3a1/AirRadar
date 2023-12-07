from functions import hexToDec
import numpy as np


def crcheck(msg_hex):
    gen = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,1,0,0,1])
    l = len(gen)
    msg_bin = hexToDec(msg_hex)
    msg = np.array([int(i) for i in msg_bin])


    for i in range(len(msg)-24):
        if msg[i] == 0:
            continue
        msg[i:i+l] = np.bitwise_xor(msg[i:i+l], gen)

    rem = np.array2string(msg[-24:], separator='')[1:-1]

    if int(rem, 2) == 0:
        pass
        #print("Not Corrupted")
    else:
        pass
        #print("Corrupted")
