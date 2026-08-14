import timeit, random
import reprlib
import threading
import sys
import csv

sys.setrecursionlimit(10_000_000)
# No LRU tail optimization


""" Quicksort * N Log(N)

Take a pivot from an array that can either be first, last, or random element
Then split the array into sub arrays based on if the number is larger or smaller than the pivot
Then recursively call the function until the array is a single element then merge them all together

"""


"""
    RECURSIVE VERSIONS
"""


def quicksort_recursive(array: list) -> list:
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort_recursive(less) + [pivot] + quicksort_recursive(greater)


def quicksort_recursive_rand_pivot(array: list) -> list:
    if len(array) < 2:
        return array
    else:
        pivot = array.pop(random.randint(0, len(array) - 1))
        less = [i for i in array if i <= pivot]
        greater = [i for i in array if i > pivot]
        return quicksort_recursive(less) + [pivot] + quicksort_recursive(greater)


def quicksort_recursive_last_pivot(array: list) -> list:
    if len(array) < 2:
        return array
    else:
        pivot = array.pop()
        less = [i for i in array if i <= pivot]
        greater = [i for i in array if i > pivot]
        return quicksort_recursive(less) + [pivot] + quicksort_recursive(greater)


def median_of_three(array):
    if len(array) < 3:
        return 0
    else:
        first = array[0]
        last = array[-1]
        middle = array[len(array) // 2]
        if first < middle < last or last < middle < first:
            return len(array) // 2
        elif middle < first < last or last < first < middle:
            return 0
        else:
            return -1


def quicksort_recursive_median_of_three_pivot(array: list) -> list:
    if len(array) < 2:
        return array
    else:
        pivot = array.pop(median_of_three(array))
        less = [i for i in array if i <= pivot]
        greater = [i for i in array if i > pivot]
        return quicksort_recursive(less) + [pivot] + quicksort_recursive(greater)


# Version with no Python magic
def quicksort_recursive_rand_pivot_simplified(array: list) -> list:
    if len(array) < 2:
        return array
    else:
        smaller, equal, larger = [], [], []
        pivot = array[random.randint(0, len(array) - 1)]

        for x in array:
            if x < pivot:
                smaller.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                larger.append(x)

        return (
            quicksort_recursive_rand_pivot_simplified(smaller)
            + equal
            + quicksort_recursive_rand_pivot_simplified(larger)
        )


"""
    ITERATIVE VERSIONS * (USING A STACK)
    

    Push onto a stack the greater array until the popped array is one element
    Extend a sorted array with that element
"""


def quicksort_iterative(array) -> list:
    if len(array) < 2:
        return array
    else:
        stack = [array]  # [[1,34,3]]
        sorted_array = []
        while stack:  # [[1,34,3]]
            current_array = stack.pop()  # [1, 34, 3] , [1]
            if len(current_array) < 2:
                sorted_array += current_array  # [1]
            else:
                pivot = current_array[0]  # 1
                less = [i for i in current_array[1:] if i <= pivot]  # []
                greater = [i for i in current_array[1:] if i > pivot]  # [34, 3]
                stack.append(greater)  # [[34, 3], [1]]
                stack.append([pivot])
                stack.append(less)
        return sorted_array


def quicksort_iterative_last_pivot(array) -> list:
    if len(array) < 2:
        return array
    else:
        stack = [array]
        sorted_array = []
        while stack:
            current_array = stack.pop()
            if len(current_array) < 2:
                sorted_array += current_array
            else:
                pivot = current_array.pop()
                less = [i for i in current_array if i <= pivot]
                greater = [i for i in current_array if i > pivot]
                stack.append(greater)
                stack.append([pivot])
                stack.append(less)
        return sorted_array


def quicksort_iterative_rand_pivot(array) -> list:
    if len(array) < 2:
        return array
    else:
        stack = [array]
        sorted_array = []
        while stack:
            current_array = stack.pop()
            if len(current_array) < 2:
                sorted_array += current_array
            else:
                pivot = current_array.pop(random.randint(0, len(current_array) - 1))
                less = [i for i in current_array if i <= pivot]
                greater = [i for i in current_array if i > pivot]
                stack.append(greater)
                stack.append([pivot])
                stack.append(less)
        return sorted_array


def quicksort_iterative_median_of_three_pivot(array) -> list:
    if len(array) < 2:
        return array
    else:
        stack = [array]
        sorted_array = []
        while stack:
            current_array = stack.pop()
            if len(current_array) < 2:
                sorted_array += current_array
            else:
                pivot = current_array.pop(median_of_three(current_array))
                less = [i for i in current_array if i <= pivot]
                greater = [i for i in current_array if i > pivot]
                stack.append(greater)
                stack.append([pivot])
                stack.append(less)
        return sorted_array


def write_to_csv(func, time, sorted_arr):
    """
    Write sorting speeds to a csv with format:
    - , time1, time2, time3, time4, time5
    func1, 0.001, 0.002, 0.003, 0.004, 0.005
    func2, 0.001, 0.002, 0.003, 0.004, 0.005
    ...
    """
    print(reprlib.repr(sorted_arr))
    print(f"Writing {func}: {time} to csv with {len(sorted_arr)} elements")

    with open("__quicksort.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([len(sorted_arr), time])


def run_and_measure(func, array):
    start = timeit.default_timer()
    sorted_arr = func(array)
    total = timeit.default_timer() - start

    write_to_csv(func.__name__, total, sorted_arr)


if __name__ == "__main__":
    with open(
        "FOO.txt",
        "r",
    ) as file:
        array = [int(line) for line in file]

    for i in range(5000, len(array), 5000):
        # start a new thread and write the time required to iterate over each range in array
        threading.Thread(
            target=run_and_measure(
                # change the function here
                quicksort_iterative_median_of_three_pivot,
                array[:i],
            )
        ).start()
