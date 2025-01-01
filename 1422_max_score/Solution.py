class Solution:
    def maxScore(self, s: str) -> int:
        if s == "":
            return 0

        score = 0

        for i in range(1, len(s)):
            left_count = s[:i].count("0")
            right_count = s[i:].count("1")
        
            if left_count + right_count > score:
                score = left_count + right_count

        return score

s = "011101"

print(Solution().maxScore(s))