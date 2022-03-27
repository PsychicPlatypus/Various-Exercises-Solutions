def palindrome(num) -> bool:
    if isinstance(num, str) or num < 0:
        return "Not valid"
    check_list = []
    for i in str(num):
        if i in check_list:
            check_list.remove(i)
        else:
            check_list.append(i)
    return len(check_list) <= 1 if len(num) != 1 else False


print(palindrome(54335))