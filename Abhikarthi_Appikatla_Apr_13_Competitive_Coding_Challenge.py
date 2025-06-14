# Program 1
def reverse_string(s: str):
    answer = []
    for i in s[::-1]:
        answer.append(f"{i}")
    answer = "".join(answer)
    print(answer)


mystring = input("Enter a string: ")
reverse_string(mystring)


# Program 2
def count_vowels(sentence:str):
    number_of_vowels = 0
    sentence.lower()
    for i in sentence:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            number_of_vowels += 1
    return number_of_vowels


sentence = input("Enter a sentence: ")
print(count_vowels(sentence))


# Program 3
def is_palindrome(word: str):
    if word == word[::-1]:
        return True
    else:
        return False


sample = input("Enter a string, I will determine if it's a palindrome: ")
print(is_palindrome(sample))


# Program 4
def find_and_replace(sentence:str, found_word:str, replaced_word:str):
    sentence = list(sentence)
    " ".join(sentence)
    print(sentence)
    proper_index = sentence.index(found_word)
    sentence = sentence.pop(proper_index)
    print(sentence)
    sentence = list(sentence)
    sentence.insert(proper_index, replaced_word)
    sentence = "".join(sentence)
    print(sentence)

sentence = input("Enter a sentence: ")
found_word = input("Enter the word you want to find: ")
replaced_word = input("Enter the word you want to replace: ")
find_and_replace(sentence, found_word, replaced_word)


# Program 5
def merge_strings(s1, s2):
    ans = [s1, s2]
    ans = "".join(ans)
    return ans

fs = input("Enter your first string: ")
ss = input("Enter your second string: ")
print(merge_strings(fs, ss))
