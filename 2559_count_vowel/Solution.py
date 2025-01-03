"""
2559. Count Vowel Strings in Ranges
Medium
Topics
Companies
Hint

You are given a 0-indexed array of strings words and a 2D array of integers queries.

Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
Output: [2,3,0]
Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
The answer to the query [0,2] is 2 (strings "aba" and "ece").
to query [1,4] is 3 (strings "ece", "aa", "e").
to query [1,1] is 0.
We return [2,3,0].

Example 2:

Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
Output: [3,2,1]
Explanation: Every string satisfies the conditions, so we return [3,2,1].

 

Constraints:

    1 <= words.length <= 105
    1 <= words[i].length <= 40
    words[i] consists only of lowercase English letters.
    sum(words[i].length) <= 3 * 105
    1 <= queries.length <= 105
    0 <= li <= ri < words.length
"""
from typing import List
from collections import defaultdict

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        is_vowel = defaultdict(bool)
        is_vowel['a'] = True
        is_vowel['e'] = True
        is_vowel['i'] = True
        is_vowel['o'] = True
        is_vowel['u'] = True

        valid_map = defaultdict(bool)
        prefix_sum = [0] * (len(words) + 1)

        for i, word in enumerate(words):
            prefix_sum[i + 1] = prefix_sum[i]
            
            if is_vowel[word[0]] and is_vowel[word[-1]]:
                prefix_sum[i + 1] += 1

        res = []

        for [start, end] in queries:
            res.append(prefix_sum[end + 1] - prefix_sum[start])

        return res


words = ["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]
print(Solution().vowelStrings(words, queries))

