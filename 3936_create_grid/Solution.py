from pprint import pprint


class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [["#"] * n] * m

        grid[0] = ["."] * n

        pprint
        for i in range(len(grid)):
            grid[i][-1] = "."
            grid[i] = "".join(grid[i])

        return grid


pprint(Solution().createGrid(6, 6))
