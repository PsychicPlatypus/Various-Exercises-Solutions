class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0] * (i + 1) for i in range(query_row + 1)]
        tower[0][0] = poured

        for y in range(query_row):
            for x in range(len(tower[y])):
                excess = tower[y][x] - 1
                if excess > 0:
                    tower[y + 1][x] += excess / 2.0
                    tower[y + 1][x + 1] += excess / 2.0

        return 1 if tower[query_row][query_glass] > 1 else tower[query_row][query_glass]
