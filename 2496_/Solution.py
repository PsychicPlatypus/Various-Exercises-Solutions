from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        if strs == []:
            return 0

        max_num = 0
        for i in strs:
            if i.isdigit():
                if int(i) >= max_num:
                    max_num = int(i)

            else:
                if len(i) >= max_num:
                    max_num = len(i)

        return max_num
