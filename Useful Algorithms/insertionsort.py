import timeit
import reprlib
import threading
import sys
import csv

sys.setrecursionlimit(10_000_000)
# No LRU tail optimization


""" INSERTION SORT * O(N ^ 2)
"""


def insertion_sort_iterative(array: list) -> list:
    if len(array) < 2:
        return array

    for i in range(1, len(array)):  #  [3, 4, 5, 32, 12], i -> 1
        key = array[i]  # 4
        j = i - 1  # j -> 0
        while j >= 0 and key < array[j]: 
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


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

    with open("__insertionsort_iterative.csv", "a+") as file:
        writer = csv.writer(file)
        writer.writerow([time, len(sorted_arr)])


def run_and_measure(func, array):
    start = timeit.default_timer()
    sorted_arr = func(array)
    total = timeit.default_timer() - start

    write_to_csv(func.__name__, total, sorted_arr)


if __name__ == "__main__":
    # Run the sorting algorithm 5 times and take the average
    with open(
        "Task1/nums.txt",
        "r",
    ) as file:
        array = [int(line) for line in file]

    for i in range(535000, len(array) + 1, 5000):
        # start a new thread and write the time required to iterate over each range in array
        threading.Thread(
            target=run_and_measure(
                # change the function here
                insertion_sort_iterative,
                array[:i],
            )
        ).start()
