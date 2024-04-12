from itertools import permutations
from collections import defaultdict


"""
Save sorted strings as keys
"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        pairs = defaultdict(None)

        for str_ in strs:
            sorted_str = "".join(sorted(str_))

            try:
                curr = pairs[sorted_str]
                curr.append(str_)
                pairs[sorted_str] = curr

            except KeyError:
                pairs[sorted_str] = [str_]

        return pairs.values()
