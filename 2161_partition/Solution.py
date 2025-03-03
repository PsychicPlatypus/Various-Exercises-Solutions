from typing import *


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # Dumb solution

        left = []
        right = []
        center = []

        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                center.append(num)

        return left + center + right
    
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
