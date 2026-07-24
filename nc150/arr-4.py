from typing import *


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


print(Solution().groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
