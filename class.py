def encript(text,shift):
    final_encription = []
    alphebet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for i in list(text):
        index = alphebet.index(i)
        b = index + shift
        index = b%26
        final_encription.append(alphebet[index])
    final_encription = "".join(final_encription)
    return final_encription
def decript(text,shift):
    final_encription = []
    alphebet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for i in list(text):
        index = alphebet.index(i)
        b = index - shift
        index = b % 26
        final_encription.append(alphebet[index])
    final_encription = "".join(final_encription)
    return final_encription
txt = input("Enter Text")
shift = int(input("Enter Shift"))
a = encript(txt, shift)
print(a)

