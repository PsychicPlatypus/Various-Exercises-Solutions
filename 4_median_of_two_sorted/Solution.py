from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        full_array = sorted(nums1)
        total = len(full_array)

        if total % 2 == 1:
            return float(full_array[total // 2])

        middle1 = full_array[total // 2 - 1]
        middle2 = full_array[total // 2]
        return (float(middle1) + float(middle2)) / 2.0


"""

median at ( lenx + leny ) / 2

"""
