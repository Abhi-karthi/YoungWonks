def falling_snow(line, rows, columns):
    lists = []
    s_list = []
    s_tempr = 0

    for i in line:
        lists.append(list(i))

    for i in range(columns):
        for x in lists:
            if x[i] == "S":
                s_tempr += 1
                # print(s_tempr)

        s_list.append(s_tempr)
        s_tempr = 0

    new_list = []
    total_list = []
    print(s_list)
    for i in range(columns):
        number = rows - s_list[i]
        new_list = []
        for x in range(rows):
            if (rows - x) > number:
                new_list.append("S")
            else:
                new_list.append(".")

        total_list.append(new_list)


    for i in range(rows)[::-1]:
        for x in range(columns):
            print(total_list[x][i], end="")
        print()



line1 = list(input())
lines = []
rows = int(line1[0])
columns = int(line1[2])
for i in range(columns + 1):
    x = input()
    lines.append(x)

falling_snow(lines, rows, columns)