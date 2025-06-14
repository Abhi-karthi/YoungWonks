def question1(n: int, p: int, d: int):
    n_str = str(n)
    if int(n_str[-p]) <= 4:
        u_sum = int(str(int(str(n)[-p]) + d)[-1])
        n_str = int(n_str)
        n_str += d
        n_str = str(n_str)
        n_str = list(n_str)
        n_str[-p] = u_sum
        for i in n_str:
            if n_str.index(i) > n_str.index(n_str[-p]):
                n_str[n_str.index(i)] = 0
        fin = ""
        for i in n_str:
            fin = fin + str(i)
        return int(fin)

    else:
        u_diff = int(str(abs(int(str(n)[-p])-d))[0])
        n_str = list(n_str)
        n_str[-p] = u_diff
        fin = ""

        for i in n_str:
            if n_str.index(i) > n_str.index(n_str[-p]):
                n_str[n_str.index(i)] = 0
        for i in n_str:
            fin = fin + str(i)
        return int(fin)


n_ = int(input("What would you like to input as n: "))
p_ = int(input("What would you like to input as p: "))
d_ = int(input("What would you like to input as d: "))
print(question1(n_, p_, d_))
