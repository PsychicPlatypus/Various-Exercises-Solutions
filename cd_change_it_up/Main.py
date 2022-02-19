def changer(s):
    final_list = []
    for i in s:
        if i.upper() == "Z":
            final_list.append("A")
        elif (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
            chars_final = chr(ord(i)+1)
            final_list.append(chars_final.upper() if (chars_final.upper() in "AEIOU") else chars_final.lower())
        else:
            final_list.append(i)
    return "".join(final_list)

print(changer("CAT3432"))
