from itertools import permutations


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        results, cache = [], []
        for i in strs:
            if i not in cache:
                grouped_perms = []
                all_permutations = ["".join(j) for j in permutations(i)]
                cache.extend(all_permutations)
                # print(all_permutations)

                for j in all_permutations:
                    if strs.__contains__(j):
                        grouped_perms.extend([j] * strs.count(j))

                results.append(grouped_perms)

        return list(filter(lambda x: x != [], results))


print(Solution().groupAnagrams(["eat", "eat", "tea", "tan", "ate", "nat", "bat"]))
