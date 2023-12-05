class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0

        for word in words:
            current_check = [i for i in chars]
            current = 0

            for char_ in word:
                if char_ not in current_check:
                    current = 0
                    break
                else:
                    current_check.remove(char_)
                    current += 1

            total += current

        return total
