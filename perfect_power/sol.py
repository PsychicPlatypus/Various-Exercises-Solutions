import math


def isPP(n):
    exponents = [i for i in range(2, int(math.log(n, 2)) + 1)]

    for i in exponents:
        if int(round(n ** (1.0 / i))) ** i == n:
            return [round(n ** (1.0 / i)), i]


print(isPP(6))
