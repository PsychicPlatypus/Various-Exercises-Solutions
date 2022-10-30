from unittest import result


def addBinary(a: str, b: str) -> str:
    to_int = [i for i in str(int(a) + int(b))]
    result = []

    for i in range(len(to_int) - 1, -1, -1):

        if i == 0:
            if to_int[i] == "3":
                result.extend(["1", "1"])
            elif to_int[i] == "2":
                result.extend(["0", "1"])
            else:
                result.append(to_int[i])
            break

        if to_int[i] == "3":
            result.append("1")
            to_int[i - 1] = str(int(to_int[i - 1]) + 1)

        elif to_int[i] == "2":
            result.append("0")
            to_int[i - 1] = str(int(to_int[i - 1]) + 1)

        else:
            result.append(str(to_int[i]))

    return "".join(reversed(result))


print(addBinary("111", "111"))
