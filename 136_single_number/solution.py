from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        t = {x for n, x in enumerate(nums) if x in nums[:n]}
        return t.symmetric_difference(set(nums)).pop()
    
test = Solution()
print(test.singleNumber([4,1,2,1,2]))