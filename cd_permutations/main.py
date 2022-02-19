from itertools import permutations as perms
from typing import List

def permutations(string: str) -> list:
    return sorted(["".join(i) for i in set(perms(string))])

permutations("aabc")