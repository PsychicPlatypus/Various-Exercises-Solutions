from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        # 1657. Determine if Two Strings Are Close
        Two strings are considered close if you can attain one from the other using the following operations:

        ## Operation 1: Swap any two existing characters.
        - For example, abcde -> aecdb
        ## Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
        - For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

        You can use the operations on either string as many times as necessary.

        Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

        ### Args:
            word1 (str): _description_
            word2 (str): _description_

        ### Returns:
            bool: _description_
        """
        if len(word1) != len(word2):
            return False

        counter1 = Counter(word1)
        counter2 = Counter(word2)
        values1 = sorted(counter1.values())
        values2 = sorted(counter2.values())
        keys1, keys2 = counter1.keys(), counter2.keys()
        return values1 == values2 and keys1 == keys2
