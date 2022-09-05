from typing import List


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        lookup_word = ""
        result_list = []
        lex_products = sorted(products, key=str.lower)
        for i in searchWord:
            current_list = []
            found_counter = 0
            lookup_word += i
            for j in range(0, len(products)):
                if found_counter == 3:
                    break
                elif lookup_word == lex_products[j][0 : len(lookup_word)]:
                    found_counter += 1
                    current_list.append(lex_products[j])
            result_list.append(current_list)
        return result_list


Solution().suggestedProducts(
    ["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"
)
