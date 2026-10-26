from typing import *


class Solution:
    # ["Hello","World"]
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s))
            encoded += "#"
            encoded += s

        # "5#Hello5#World"
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        # "5#Hello5#World"
        decoded = []
        i = 0

        while i < len(s):
            curr = i  # 0
            while s[curr] != "#":
                curr += 1
            length = int(s[i:curr])
            i = curr + 1
            curr = i + length
            decoded.append(s[i:curr])
            i = curr

        return decoded
