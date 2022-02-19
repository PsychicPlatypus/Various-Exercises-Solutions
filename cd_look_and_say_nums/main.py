from itertools import count

memory = []
def look_and_say(data, maxlen):
    global memory
    next_data, counter = [], 1
    for i in range(len(data)):
        try:
            if data[i + 1] == data[i]:
                counter -=- 1
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


print(look_and_say("132", 5))