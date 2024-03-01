"""
Input: s = "010"
Output: "001"
Explanation: Because there is just one '1', it must be in the last position. So the answer is "001".

Input: s = "0101"
Output: "1001"
Explanation: One of the '1's must be in the last position. The maximum number that can be made with the remaining digits is "100". So the answer is "1001".
"""


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = sorted(s, reverse=True)
        if s[-1] == 1:
            return "".join(s)

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "1":
                s[i] = "0"
                s[len(s) - 1] = "1"
                return "".join(s)


print(Solution().maximumOddBinaryNumber("010"))

print(Solution().maximumOddBinaryNumber("1"))
print(
    Solution().maximumOddBinaryNumber(
        "1100010010001010011001100110100111000001010101110110111011011101100000010110110100001111011110110100"
    )
)
print(
    Solution().maximumOddBinaryNumber(
        "1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"
    )
)
print(
    Solution().maximumOddBinaryNumber(
        "1111111111111111111111111111111111111111111111111100000000000000000000000000000000000000000000000000"
    )
)
print(
    Solution().maximumOddBinaryNumber(
        "1111111111111111111111111111111111111111111111111100000000000000000000000000000000000000000000000001"
    )
)
print(
    Solution().maximumOddBinaryNumber(
        "0111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111110"
    )
)
print(
    Solution().maximumOddBinaryNumber(
        "0101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101"
    )
)
print(
    Solution().maximumOddBinaryNumber(
        "1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010"
    )
)
print(
    Solution().maximumOddBinaryNumber(
        "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000110"
    )
)
