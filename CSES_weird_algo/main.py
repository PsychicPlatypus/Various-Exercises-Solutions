def weird_algo(n):
    actions = [n]
    while n > 1:
        if n % 2 == 0:
            n /= 2
            actions.append(int(n))
        else:
            n = (n * 3) + 1
            actions.append(int(n))
    print (" ".join([str(i) for i in actions]))

weird_algo(int(input()))