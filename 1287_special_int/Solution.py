from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        quarter = n // 4

        for i in range(n - quarter):
            # If num is present in 3/4 and 1/4 then return it
            if arr[i] == arr[i + quarter]:
                return arr[i]

        return -1
