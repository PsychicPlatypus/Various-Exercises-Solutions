class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        rows = [[1], [1, 1]]
        for i in range(1, numRows - 1):
            new_row = [1]

            prev = rows[i]
            for j in range(len(prev)):
                if j == len(prev) - 1:
                    break
                new_row.append(prev[j] + prev[j + 1])

            new_row.append(1)
            rows.append(new_row)

        return rows


print(Solution().generate(5))
