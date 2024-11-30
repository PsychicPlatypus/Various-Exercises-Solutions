from typing import List
from collections import defaultdict

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        record = defaultdict(int)
        champion = -1

        for match in edges:
            [_, team_y] = match
            record[team_y] -= 1

        for contestant in range(n):
            result = record[contestant]

            if result == 0 and champion == -1:
                champion = contestant
            elif result == 0:
                return -1

        return champion

print(Solution().findChampion(3, [[2, 0]]))