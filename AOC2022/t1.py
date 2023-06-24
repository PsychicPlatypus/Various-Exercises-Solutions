with open(
    "/Users/dzenis.madzovic/Desktop/Other Projects/CodeWars-2021/AOC2022/t1.txt", "r"
) as f:
    data = f.read().splitlines()


def calc(ls):
    ls.append("")
    largest = []
    current = 0
    for i in ls:
        if i != "":
            current += int(i)
        else:
            largest.append(current)
            current = 0

    largest.sort(reverse=True)
    print(largest[0] + largest[1] + largest[2])


calc(data)
