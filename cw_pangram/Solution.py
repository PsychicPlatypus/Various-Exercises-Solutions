def is_pangram(s: str) -> bool:
    all_letters = {i for i in "ABCDEFGHIJKLMNOPQRSTUWZYX"}
    sentence_letters = set()
    for i in s:
        if i in all_letters:
            sentence_letters.add(i)

    return True if len(sentence_letters) == len(all_letters) else False
