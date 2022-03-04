def solution(string, markers):
    print(string)
    words = string.split("\n")
    while markers:
        words = [i.split(markers[0])[0] for i in words]
        markers.pop(0)
    return "\n".join(words)

print(solution("strawberries strawberries\ncherries\napples oranges\npears cherries bananas\navocados apples ' apples watermelons watermelons"
         , ['#', ',', '@', '.', '?', '=', '!', '-', "'"]))