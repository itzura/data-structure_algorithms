from stackimplement import Stack

def parchecker(key):
    s = Stack()
    index = 0
    balanced = True
    while index<len(key) and balanced:
        symbol = key[index]
        if symbol in "([{<":
            s.push(symbol)
        elif symbol in ")]}>":
            if s.isEmpty():
                balanced = False
            else:
                if not matches(s.pop(),symbol):
                    balanced = False
                    break
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{<"
    closes = ")]}>"
    return opens.index(open) == closes.index(close)

print(parchecker("{}([{<>}()])")) 