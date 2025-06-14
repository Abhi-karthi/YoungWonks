# Program 1
def remove_vowel(names: list):
    for i in names:
        i.lower()
        if "a" in i:
            names.remove(i)
        elif "e" in i:
            names.remove(i)
        elif "i" in i:
            names.remove(i)
        elif "o" in i:
            names.remove(i)
        elif "u" in i:
            names.remove(i)
    return names


sample_input = ['Alice', 'Lyn', 'Bryn', 'Jake', "Gwyn"]
sample_input = remove_vowel(sample_input)
print(sample_input)
# Program 2


def remove_fives(integers: list[int, int, int, int, int, int, int, int, int, int]):
    acceptable = True
    for i in integers:
        if i > 100:
            acceptable = False
        if i < 1:
            acceptable = True
    if acceptable:
        for i in integers:
            a = str(i)
            if "5" in a:
                integers.remove(i)
    return integers


sample_input = [12, 34, 45, 23, 25, 67, 89, 90, 10, 15]
sample_input = remove_fives(sample_input)
print(sample_input)
# Program 3


def replace_vowels_with_spaces(names: list):
    for i in names:
        temp = list(i.lower())
        for x in list(i.lower()):
            if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
                temp[i.find(x)] = " "
            names[names.find(i)] = temp
            # if x == "a":
            #     temp = list(i)
            #     temp.remove("a")
            #     temp.insert(i.index(x), " ")
            #     temp = "".join(i)
            #     names[names.index(i)] = temp
            # if x == "e":
            #     temp = list(i)
            #     temp.remove("e")
            #     temp.insert(i.index(x), " ")
            #     temp = "".join(i)
            #     names[names.index(i)] = temp
            # if x == "i":
            #     temp = list(i)
            #     temp.remove("i")
            #     temp.insert(i.index(x), " ")
            #     temp = "".join(i)
            #     names[names.index(i)] = temp
            # if x == "o":
            #     temp = list(i)
            #     temp.remove("o")
            #     temp.insert(i.index(x), " ")
            #     temp = "".join(i)
            #     names[names.index(i)] = temp
            # if x == "u":
            #     temp = list(i)
            #     temp.remove("u")
            #     temp.insert(i.index(x), " ")
            #     temp = "".join(i)
            #     names[names.index(i)] = temp
    return names


sample_input = ['Alice', 'Lyn', 'Bryn', 'Jake', 'Gwyn']
sample_input = replace_vowels_with_spaces(sample_input)
print(sample_input)
