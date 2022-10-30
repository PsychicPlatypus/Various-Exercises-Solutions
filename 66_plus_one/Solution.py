from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [i for i in str(int("".join([str(i) for i in digits])) + 1)]


if __name__ == "__main__":
    print(Solution().plusOne([4, 3, 2, 1]))
