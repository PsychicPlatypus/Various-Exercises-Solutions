def circle_slash(n: int) -> int:
    members = list(range(1, n + 1))
    index = 0
    while len(members) > 1:
        index = (index + 2 - 1) % len(members)
        members.pop(index)
    return members[0]
