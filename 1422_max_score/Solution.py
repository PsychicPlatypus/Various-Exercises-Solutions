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


class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count("1")
        zeroes = 0
        score = 0

        for i in range(len(s) - 1):
            if s[i] == "1":
                ones -= 1
            
            if s[i] == "0":
                zeroes += 1

            if ones + zeroes > score:
                score = ones + zeroes

        return score

    
s = "011101"

print(Solution().maxScore(s))