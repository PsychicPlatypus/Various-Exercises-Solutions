class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        x = int("".join([i for i in reversed(str(abs(x)))]))

        if neg:
            x = x * -1

        if x > pow(2, 31) or x < -(pow(2, 31)):
            return 0

        return x
