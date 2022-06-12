from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    if target not in nums:
        x = int(len(nums)/2)
        if target > nums[x]:
            for i in range(x + 1, len(nums)):
                if nums[i] > target:
                    return i
            return len(nums)
        for i in range(x - 1, -1, -1):
            if nums[i] < target:
                return i + 1
        return 0
    else:
        return nums.index(target)

print (searchInsert([1,3,5,7,8,10,11,15,26,47,68], 6))