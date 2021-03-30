from stackimplement import Stack

def binarycon(deckey):
    remstack = Stack()

    while deckey > 0:
        rem = deckey%2
        remstack.push(rem)
        deckey = deckey //2

    binstring = ""
    while not remstack.isEmpty():
        binstring += str(remstack.pop())

    return binstring

print(binarycon(21))

