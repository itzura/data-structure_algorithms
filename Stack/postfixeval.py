from stackimplement import Stack

def postfixEval(postfixexp):
    operandstack = Stack()
    tokenlist = postfixexp.split()

    for token in tokenlist:
        if token in "0123456789":
            operandstack.push(token)
        else:
            operand2 = operandstack.pop()
            operand1 = operandstack.pop()
            result  = doMath(token, int(operand1), int(operand2))
            operandstack.push(result)
    return operandstack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1*op2
    elif op=="/":
        return op1/op2
    elif op=="+":
        return op1 + op2
    else:
        return op1-op2

print(postfixEval("7 8 +"))
