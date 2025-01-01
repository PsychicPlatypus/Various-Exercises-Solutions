"""
You are given a list of strings of the same length words and a string target.

Your task is to form target using the given words under the following rules:

    1. target should be formed from left to right. +

    2. To form the i-th character (0-indexed) of target,
     you can choose the kth character of the jth string in words if target[i] = words[j][k].
    3. Once you use the kth character of the jth string of words,
     you can no longer use the xth character of any string in words where x <= k.
      In other words, all characters to the left of or at index k become unusuable for every string.
    4. Repeat the process until you form the string target.

Notice that you can use multiple characters from the same string in words provided the conditions above are met.

Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.
                   -->
        target = "aba"

        _ _ _
        2
        1

Example 1:

Input: words = ["acca","bbbb","caca"], target = "aba"
Output: 6
Explanation: There are 6 ways to form target.
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")

Example 2:

Input: words = ["abba","baab"], target = "bab"
Output: 4
Explanation: There are 4 ways to form target.
"bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
"bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
"bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
"bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")

 
"""
from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        count_letters = 0

        for word in words:
            if target[0] in word:
                count_letters += 1
                word = word[1:]




words = ["abba","baab"]
target = "bab"

Solution().numWays(words, target)






















