from dequeimplement import Deque

def palindromecheck(key):
    d = Deque()
    isPalindrome = True
    for token in key:
        d.addFront(token)

    while d.size() > 1 and isPalindrome:
        front = d.removeFront()
        rear = d.removeRear()
        if front != rear:
            isPalindrome = False
            break
    return isPalindrome

print(palindromecheck("itzuraruzti"))
