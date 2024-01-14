class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        odd = self.__largest_odd_palindrome_finder(s)
        even = self.__largest_even_palindrome_finder(s)
        if len(odd) >= len(even):
            return odd
        else:
            return even

    def __largest_odd_palindrome_finder(self, s: str) -> str:
        longest = s[0]
        palindrome_locations = []

        for i in range(len(s) - 2):
            if s[i] == s[i + 2]:
                palindrome_locations.append(i + 1)

        for i in palindrome_locations:
            low = i - 1
            high = i + 1

            while low >= 0 and high < len(s):
                if s[low] == s[high]:
                    low -= 1
                    high += 1
                else:
                    break

            if len(s[low + 1 : high]) >= len(longest):
                longest = s[low + 1 : high]

        return longest

    def __largest_even_palindrome_finder(self, s: str) -> str:
        longest = s[0]
        palindrome_locations = []

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                palindrome_locations.append(i)

        for i in palindrome_locations:
            low = i
            high = i + 1

            while low >= 0 and high < len(s):
                if s[low] == s[high]:
                    low -= 1
                    high += 1
                else:
                    break

            if len(s[low + 1 : high]) >= len(longest):
                longest = s[low + 1 : high]

        return longest
