from collections import defaultdict
import heapq
from typing import *

LIMIT = 100


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurances = defaultdict(int)

        for num in nums:
            occurances[num] += 1
            print(occurances)

        res = []

        for _ in range(k):
            max_o_n = max(occurances.values())

            key = next((k for k, v in occurances.items() if v == max_o_n), None)
            occurances.pop(key)
            res.append(key)

        return res


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurances = defaultdict(int)

        for num in nums:
            occurances[num] += 1

        heap = []
        for num in occurances.keys():
            heapq.heappush(heap, (occurances[num], num))
            print(heap)
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


nums = [1, 2, 2, 3, 3, 3]
k = 2

print(Solution().topKFrequent(nums=nums, k=k))
