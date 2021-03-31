def isPal(palstring):
    b = 0
    e = -1
    if(palstring[b] != palstring[e]):
        return False
    else:
        b +=1
        e -=1

    while(b<e+1):
        return isPal(palstring)
    return True

print(isPal("radar"))