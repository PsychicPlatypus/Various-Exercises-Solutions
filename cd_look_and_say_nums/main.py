memory = []


def look_and_say(data, maxlen):
    global memory
    next_data, counter = [], 1
    for i in range(len(data)):
        try:
            if data[i + 1] == data[i]:
                counter -= -1
            else:
                next_data.append(str(counter) + data[i])
                counter = 1
        except IndexError:
            next_data.append(str(counter) + data[i])
    maxlen -= 1
    memory.append("".join(next_data))
    if maxlen == 0:
        return_list, memory = memory, []
        return return_list
    else:
        return look_and_say("".join(next_data), maxlen)


def sss(ls, maxlen):
    global memory
    counter, current = 1, []

    for i in range(len(ls)):
        try:
            if ls[i] == ls[i + 1]:
                counter += 1
            else:
                current.append(str(counter) + str(ls[i]))
                counter = 1
        except IndexError:
            current.append(str(counter) + str(ls[i]))

    maxlen -= 1
    to_string = "".join(current)
    memory.append(to_string)
    return memory if maxlen == 0 else sss("".join(to_string), maxlen)


print(sss("132", 5))
