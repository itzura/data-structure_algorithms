from stackimplement import Stack

def baseconvertor(decikey, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()
    while decikey > 0:
        rem = decikey%base
        remstack.push(rem)
        decikey = decikey // base

    converted = ""
    while not remstack.isEmpty():
        converted += digits[remstack.pop()]

    return converted

print(baseconvertor(13,2))