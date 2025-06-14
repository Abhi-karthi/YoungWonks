a = 'Hello there, I hope you are having a nice day. '
word = ''
list = []
for i in a:
    word = word + i
    if i == " ":
        list.append(word)
        word = ''
for i in range(len(list)):
    print(list[i])