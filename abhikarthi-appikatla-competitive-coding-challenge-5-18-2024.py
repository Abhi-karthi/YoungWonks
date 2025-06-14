# Program 1
def find_missing_character(input_string: str):
    input_string = list(input_string.lower())
    completed_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(input_string)):
        if input_string[i] != completed_list[i]:
            return completed_list[i]


sample_input = "abcdefghijklmnoqrstuvwxyz"
print(find_missing_character(sample_input))
# Program 2


def first_non_repeating_character(input_string):
    for i in input_string:
        for x in input_string:
            
