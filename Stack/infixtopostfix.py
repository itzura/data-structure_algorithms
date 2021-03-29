from stackimplement import Stack

def infixToPostfix(key):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opstack =Stack()
    postfixlist=[]
    tokenlist = key.split()
    for token in tokenlist:

        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or \
            token in "0123456789":
            postfixlist.append(token)
        
        elif token =="(":
            opstack.push(token)
        
        elif token == ")":
            toptoken = opstack.pop()
            
            while toptoken != "(":
                postfixlist.append(toptoken)
                toptoken= opstack.pop()
        
        else:
            
            while (not opstack.isEmpty()) and \
                (prec[opstack.peek()]>=prec[token]):
                postfixlist.append(opstack.pop())
            opstack.push(token)
    while not opstack.isEmpty():
        postfixlist.append(opstack.pop())
    return " ".join(postfixlist)

print(infixToPostfix("A + B - C * D"))