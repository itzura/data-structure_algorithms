import sys
sys.path.insert(1,'C:/Users/Rohan/data-structure_algorithms/Linear_Structures/Stack')
from stackimplement import Stack
s = Stack()
def palStr(n, base):
    convertString = "0123456789ABCDEF"
    while n>0:
        if n<base:
            s.push(convertString[n])
        else:
            s.push(convertString[n%base])
        n = n//base
    result = ""
    while not s.isEmpty():
        result += s.pop()
    return result
print(palStr(1599,16))
