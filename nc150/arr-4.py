from typing import *
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        sorted_anagrams = dict()

        for str in strs:
            # "cat"
            sorted_str = "".join(sorted(str))

            if sorted_anagrams.get(sorted_str) == None:
                sorted_anagrams[sorted_str] = [str]

            else:
                sorted_anagram: List = sorted_anagrams[sorted_str]
                sorted_anagram.append(str)

        return list(sorted_anagrams.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - 97] += 1  # from 97, all lowercase ascii letters
            res[tuple(count)].append(s)
        return list(res.values())


print(Solution().groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
