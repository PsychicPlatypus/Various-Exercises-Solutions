class Solution(object):
    def romanToInt(self, s):
        mapped_romans = {
            "I": 1,
            "V": 5,
            "IV": 4,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        number, skip_this_iteration = 0, False
        for j, i in enumerate(s):
            print(s, number)
            if skip_this_iteration:
                skip_this_iteration = False
                continue
            try:
                if mapped_romans.get(i + "" + s[j + 1]) != None:
                    number += mapped_romans.get(i + s[j + 1])
                    skip_this_iteration = True
                else:
                    number += mapped_romans.get(i)
            except IndexError:
                number += mapped_romans.get(i)
        return number


test = Solution()
test.romanToInt("DCXXI")
