from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        occurrences = defaultdict(int)

        for char_s, char_t in zip(s, t):
            occurrences[char_s] += 1
            occurrences[char_t] -= 1

        for i in occurrences.values():
            if i != 0:
                return False

        return True


class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


solution = Solution().isAnagram

print(solution("racecar", "carrace"))
print(solution("jar", "jam"))
