# ABHIKARTHI APPIKATLA 3-30-2024 COMPETITIVE CODING CHALLENGE

# Program 1

def list_intersection(list1, list2):
    a = list1.split(" ")
    b = list2.split(" ")
    intersections = []
    pastintersections = []
    for i in a:
        for x in b:
            if i == x and i not in pastintersections:
                intersections.append(i)
                pastintersections.append(i)
    print(intersections)

l1 = input("Enter multiple integers seperated with a space (first list).")
l2 = input("Enter multiple integers seperated with a space (second list).")
list_intersection(l1, l2)

# Program 2

def remove_duplicates_from_list(mylist):
    uniquelist = mylist.split(" ")
    uniquelist.pop(0)
    pastlist = []
    for i in uniquelist:
        if i not in pastlist:
            uniquelist.remove(i)
            pastlist.append(i)
    print(uniquelist)

list = input("Enter a series of integers seperated by spaces: ")
remove_duplicates_from_list(list)

# Program 3

def transpose_a_matrix(dimensions, rows):
    dimensions = dimensions.split(" ")
    output = []
    for i in rows:
        for x in i:
            x.append(output)

# Program 4

def merge_two_lists_arternately(list1, list2):
    list1 = list1.split(' ')
    list2 = list2.split(' ')
    turn = 0
    a = 0
    b = 0
    output = []
    for i in range(len(list1) + len(list2)):
        if turn == 0 and a < len(list1):
            output.append(list1[a])
            a += 1
            turn = 1
        else:
            output.append(list2[b])
            b += 1
            turn = 0
    print(output)

l1 = input("Enter multiple integers seperated with a space (first list).")
l2 = input("Enter multiple integers seperated with a space (second list).")

merge_two_lists_arternately(l1, l2)

# Program 5

def rotate_a_2d_list(dimensions, rows):
    dimensions = dimensions.split(" ")
    rows = rows.split(" ")
    output = []
    for i in range(dimensions[0]):
        for x in range(dimensions[1]):
            output.append([rows[x]])