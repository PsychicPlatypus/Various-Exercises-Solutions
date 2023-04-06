from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        return self.calculate_answer(grid, 0)

    def calculate_answer(self, grid: List[List[int]], answer: int) -> int:
        if grid[0] == []:
            return answer

        current_max = 0
        for i in grid:
            maximum_int = max(i)
            if maximum_int >= current_max:
                current_max = maximum_int

            i.remove(maximum_int)

        answer += current_max
        return self.calculate_answer(grid, answer)


print(Solution().deleteGreatestValue([[1, 2, 4], [3, 3, 1]]))
