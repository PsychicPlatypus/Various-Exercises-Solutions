from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        Find all duplicates in an array of integers.
        Let's analyze the time and space complexity of the provided solution:
        ## Time Complexity:

        - The code iterates through the input list nums once with a loop, visiting each element once. This loop runs in linear time O(n), where n is the length of the input list.
        - Inside the loop, there are constant time operations for accessing and updating elements in the marked list and appending elements to the duplicates list. These operations do not affect the overall time complexity.
        - Therefore, the overall time complexity of the code is O(n).

        ## Space Complexity:

        - The code creates two additional lists: marked, which is the same length as the input list nums, and duplicates, which stores the duplicate elements found. Thus, it uses additional space proportional to the size of the input list and the number of duplicate elements.
        - In the worst-case scenario where there are no duplicates, the space complexity would be O(n) for the marked list and O(1) for the duplicates list.
        - In the best-case scenario where all elements are duplicates, the space complexity would be O(n) for both lists.
        - Therefore, the space complexity can be considered as O(n), where n is the length of the input list.

        ## In summary:

        - Time Complexity: O(n)
        - Space Complexity: O(n)

        ## Args:
            nums (List[int]): _description_

        ## Returns:
            List[int]: _description_
        """
        duplicates = []
        marked = [0] * len(nums)

        for i in range(0, len(nums)):
            mark = nums[i]
            if marked[mark - 1] == -1:
                duplicates.append(mark)
            marked[mark - 1] = -1

        return duplicates
