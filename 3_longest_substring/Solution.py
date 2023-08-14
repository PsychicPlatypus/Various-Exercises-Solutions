class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_longest = 0
        current_substring = ""

        for i in s:
            print(current_substring)
            if not i in current_substring:
                current_substring += i
            else:
                if len(current_substring) > current_longest:
                    current_longest = len(current_substring)
                current_substring = i

        return (
            current_longest
            if current_longest > len(current_substring)
            else len(current_substring)
        )


print(Solution().lengthOfLongestSubstring(" "))
