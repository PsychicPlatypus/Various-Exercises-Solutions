class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res_matrix = [["-" for _ in range(len(s))] for _ in range(numRows)]
        index_y = 0
        index_x = 0
        _diag = False
        res = ""

        for char in s:
            res_matrix[index_y][index_x] = char

            if _diag and index_y == 0:
                _diag = False
                index_y += 1
            elif _diag:
                index_y -= 1
                index_x += 1
            elif index_y == numRows - 1:
                index_y -= 1
                index_x += 1
                _diag = True
            else:
                index_y += 1

        
        for row in res_matrix:
            res += "".join(row).replace("-", "")

        return res

        
s = "PAYPALISHIRING"; numRows = 3   

print(Solution().convert(s, numRows))

"""
0
1   7
2  6
3 5
4

0
1    9
2   8
3  7
4 6
5
"""
# 1 -> 3 -> 5 -> 7 -> 9
# 2 -> 3 -> 4 -> 5 -> 6