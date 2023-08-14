import heapq


class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        # 1 <= k <= nums.length <= 105
        if k == 0 or k > len(nums) + 1:
            return 0

        # Cut array in 2 (one kth size) and min-heapify
        heapq.heapify(kth_heap := nums[:k])

        for i in nums[k:]:
            # If bigger than smallest
            if i > kth_heap[0]:
                heapq.heappushpop(kth_heap, i)

        return kth_heap[0]


print(Solution().findKthLargest([1, 2, 3, 4, 5], 3))
