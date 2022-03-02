
from operator import ne


def find(needle, haystack):
    search_word = needle.strip("_")
    if needle and search_word not in haystack:
        return -1
    elif "_" not in needle:
        return haystack.find(needle)
    adder = 0
    for i in needle:
        if i != "_":
            break
        adder += 1
    
    return haystack.find(search_word) - adder
    

print(find("_po_", "Once upon a midnight dreary, while I pondered, weak and weary"))
    
    