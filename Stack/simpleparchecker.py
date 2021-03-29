from stackimplement import Stack

def parchecker(key):
    s= Stack()
    balanced = True
    index = 0
    while index<len(key) and balanced:
        symbol = key[index]
        if symbol == "(":
            s.push(symbol)
        elif symbol == ")":
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index +=1
    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parchecker("yo(())"))
