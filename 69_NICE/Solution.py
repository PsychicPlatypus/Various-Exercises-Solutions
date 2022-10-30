import math


class Solution:
    def mySqrt(self, x: int) -> int:
        # x >= 0
        return math.floor(math.sqrt(x))

    def mySqrt2(self, x: int) -> int:
        # x >= 0
        # This solution doesn't work because it rounds on int
        # so bassically its more accurate than it needs to be :)
        if True:
            pass
        closest_number = 0
        previous_difference = 99999999999999999
        for i in range(0, int(x / 2)):
            power = i * i
            difference = abs(x - power)
            if difference < previous_difference:
                closest_number = i
                previous_difference = difference
            else:
                break

        return closest_number


print(Solution().mySqrt2(432143))
