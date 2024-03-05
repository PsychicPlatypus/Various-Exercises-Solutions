class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1

        while left < right and s[left] == s[right]:
            c_l = s[left]

            while left <= right and s[left] == c_l:
                left += 1

            while right >= left and s[right] == c_l:
                right -= 1

        return right - left + 1
