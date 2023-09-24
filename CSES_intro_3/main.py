seq = input()
curr = 0
max_ = 0
for i in range(len(seq)):
    if i == len(seq) - 1:
        curr += 1
        if curr > max_:
            max_ = curr
        break
    if seq[i + 1] == seq[i]:
        curr += 1
    else:
        curr += 1
        if curr > max_:
            max_ = curr
        curr = 0

print(max_)
