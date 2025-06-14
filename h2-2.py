a = "Hi, my name is Abhi."
c = list(a)
b = a.split(" ")
print(c + b)
b.insert(1, "Pras")
d = b
b.append("Bye")
print(b)
word = b.pop()
print(d)
print(c)
b.sort(reverse = True)
print(b)
print(word)

s = "".join(c)
print(s)
print(b[1:5])
print(b[5:1:-1])
print(b)
f = b[:]
b.append("a")
print(f)
print(b)