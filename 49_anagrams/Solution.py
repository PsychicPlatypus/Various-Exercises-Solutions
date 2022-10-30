class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        results = []
        for i in strs:
            if i[::-1] not in strs:
                results.append([i])
            else:
                results.append([i, i[::-1]])
                strs.remove(i[::-1])
        return results


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
