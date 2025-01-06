from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0] * len(boxes)

        if "1" not in boxes:
            return res

        for i, ball in enumerate(boxes):
            if ball == "1":
                res_front = res[:i]
                res_front.reverse()
                res_front = self.prefixSum(res_front)
                res_front.reverse()

                res_back = res[i + 1 :]
                res_back = self.prefixSum(res_back)

                res = res_front + [res[i]] + res_back

        return res

    def prefixSum(self, res: List[int]) -> List[int]:
        if res == []:
            return []

        i = 0
        val = 1
        lenght = len(res)

        while i < lenght:
            res[i] += val
            val += 1
            i += 1

        return res


print(Solution().minOperations("001011"))

# 001011 ->  2 1 0 1 2 3
#        ->  4 3 2 1 0 1
#        ->  5 4 3 2 1 0
#        -> 11 8 5 4 3 4
