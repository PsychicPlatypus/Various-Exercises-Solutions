class Solution(object):
    def twoSum(self, nums, target):
        answers = []
        for x, i in enumerate(nums):
            for y, j in enumerate(nums):
                if i + j == target:
                    answers.append([x,y])
        return answers