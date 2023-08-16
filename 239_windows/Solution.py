import _heapq
import collections


# class Solution:
#     def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
#         # Max heap?
#         _heapq.heapify(kth_max_heap := list(-nums[i] for i in range(0, k)))
#         print(kth_max_heap)
#         result = [-(kth_max_heap[0])]
#         for i in nums:
#             print(nums, kth_max_heap)
#             _heapq.heappush(kth_max_heap, -i)
#             result.append(-(_heapq.heappop(kth_max_heap)))

#         return result


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        max_first_queue = collections.deque()
        result = []
        for i, n in enumerate(nums):

            while max_first_queue and nums[max_first_queue[-1]] < n:
                # Pop queue until the last element is the largest
                max_first_queue.pop()

            max_first_queue.append(i)

            if max_first_queue[0] == i - k:
                # Size check
                max_first_queue.popleft()

            if i >= k - 1:
                # Pop after
                result.append(nums[max_first_queue[0]])

        return result


print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
