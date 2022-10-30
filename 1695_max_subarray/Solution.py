from tkinter import N
from typing import List


def maximumUniqueSubarray(nums: List[int]) -> int:
    """
    index = 0
    mem_var = []
    while True:
        curr_var = []
        for i in range(index, len(nums)):
            curr_var.append(nums[i])
            if i == len(nums) - 1:
                break
            elif nums[i + 1] in curr_var:
                break
        index += 1
        if len(mem_var) < len(curr_var):
            mem_var = curr_var

            if len(mem_var) + index >= len(nums):
                return sum(mem_var)
    """

    """
    You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

"""


print(maximumUniqueSubarray([4, 2, 4, 5, 6]))
