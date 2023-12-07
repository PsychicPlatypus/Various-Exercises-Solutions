import sys

sys.set_int_max_str_digits(9999999)


class Solution:
    def largestOddNumber(self, num: str) -> str:
        largest = 0

        for i in range(len(num) - 1, -1, -1):
            conv_num = int(num[i])

            if conv_num % 2 == 1:
                conv_substr = int(num[0 : i + 1])
                largest = conv_substr
                break

        return "" if largest == 0 else str(largest)
