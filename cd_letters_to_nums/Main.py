def alphabet_position(text):
    final_numbers = []
    for i in text:
        if i.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            final_numbers.append(str(ord(i.upper())-64))
    return ' '.join(final_numbers)

print(alphabet_position("acds, ffe, d"))