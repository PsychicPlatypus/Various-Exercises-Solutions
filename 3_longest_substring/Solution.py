class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        curr_subs = set()
        min_p = 0

        for max_p in range(len(s)):
            curr_char = s[max_p]
            if curr_char in curr_subs:
                # Move left pointer until you delete it
                while curr_char in curr_subs:
                    curr_subs.remove(s[min_p])
                    min_p += 1
                curr_subs.add(curr_char)
            else:
                curr_subs.add(curr_char)
                longest = len(curr_subs) if len(curr_subs) > longest else longest

        return longest


print(Solution().lengthOfLongestSubstring(" "))
