from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        w = float("inf")
        x = float("inf")
        y = 0
        z = 0

        for n in nums:
            if n < w:
                x = w
                w = n

            elif n < x:
                x = n

            if n > y:
                z = y
                y = n

            elif n > z:
                z = n

        return (z * y) - (w * x)
