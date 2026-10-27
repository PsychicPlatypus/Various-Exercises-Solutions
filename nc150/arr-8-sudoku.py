from typing import *
from collections import defaultdict


class Solution:
    # Naive solution
    checkedRows = defaultdict(bool)

    def isValidRow(self, row: List[str]) -> bool:
        row_str = "".join(row)

        print(row_str)

        if self.checkedRows[row_str]:
            return True

        row_stripped = row_str.replace(".", "").split()
        row_set = set(row_stripped)

        if len(row_stripped) == len(row_set):

            self.checkedRows[row_str] = True
            return True

        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.isValidRow(row):
                return False

        for i in range(len(board[0])):
            current_coll = []
            for row in board:
                current_coll.append(row[i])

            if not self.isValidRow(current_coll):
                return False

        ...


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_mem = defaultdict(set)
        col_mem = defaultdict(set)
        square_mem = defaultdict(set)

        for row in range(9):
            for coll in range(9):
                current = board[row][coll]

                if current == ".":
                    continue

                if (
                    current in row_mem[row]
                    or current in col_mem[coll]
                    or current in square_mem[(row // 3, coll // 3)]
                ):
                    return False

                row_mem[row].add(current)
                col_mem[coll].add(current)
                square_mem[(row // 3, coll // 3)].add(current)

        return True


board = [
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "1", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


print(Solution().isValidSudoku(board))
