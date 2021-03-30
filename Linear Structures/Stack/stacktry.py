from stackimplement import Stack
x = input()
s= Stack()
for i in x:
    s.push(i)
k = ""
while not s.isEmpty():
    k += s.pop()
print(k)
