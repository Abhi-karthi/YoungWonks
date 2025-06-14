# Program 1
def find_key_with_longest_string_value(input_dict: dict):
    mylist = []
    value = ""
    answer = ""
    for i in input_dict:
        mylist.append(input_dict[i])

    for i in mylist:
        if len(i) > len(value):
            value = i

    for i in input_dict:
        if value == input_dict[i]:
            answer = i
    return answer


sample_input = {'a': 'apple', 'b': 'banana', 'c': 'cherry pie'}
print(find_key_with_longest_string_value(sample_input))
# Program 2


def find_top_student(score_dict: dict):
    average_list = []
    add = 0
    temp = []
    for i in score_dict:
        sum(score_dict[i])