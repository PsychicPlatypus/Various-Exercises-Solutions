MEMORY = []

def sum_of_intervals(intervals):
    second_number, first_number = intervals[0][1], intervals[0][0]
    for i in intervals:
        if i[0] < second_number:
            if i[1] > second_number:
                second_number = i[1]
            elif i[0] < first_number:
                first_number = i[0]
            intervals = list(filter(lambda a: a != i, intervals))
    sum = second_number - first_number
    MEMORY.append(sum)
    if not intervals:
        sum = 0
        for i in MEMORY:
            sum += i
        MEMORY.clear()
        return sum
    return sum_of_intervals(intervals)

# My solution
def sum_of_intervals_two(intervals):
    unique_intervals = []
    for interval in intervals:
        for i in range(interval[0], interval[1]):
            if i not in unique_intervals:
                unique_intervals.append(i)

    return len(unique_intervals)

print(sum_of_intervals(
   [(1, 5), (1, 5)]
))