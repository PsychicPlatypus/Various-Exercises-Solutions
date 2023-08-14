class Solution(object):
    def summaryRanges(self, nums):
        if len(nums) <= 1:
            return [] if nums == [] else [f"{nums[0]}"]
        result, beginning = [], nums[0]
        for i in range(1, len(nums)):
            lookup_num = nums[i - 1] + 1
            if nums[i] != lookup_num and i == len(nums) - 1:
                result.append(
                    f"{beginning}->{nums[i - 1]}"
                    if beginning != nums[i - 1]
                    else f"{beginning}"
                )
                result.append(f"{nums[i]}")
            elif nums[i] != lookup_num:
                result.append(
                    f"{beginning}->{nums[i - 1]}"
                    if beginning != nums[i - 1]
                    else f"{beginning}"
                )
                beginning = nums[i]
            elif i == len(nums) - 1:
                result.append(f"{beginning}->{nums[i]}")

        return result


print(Solution().summaryRanges([0, 2, 3, 4, 6, 8]))
