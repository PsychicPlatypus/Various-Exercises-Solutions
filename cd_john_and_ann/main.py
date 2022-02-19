def this_kata_is_awful(n):
    john = [0]
    ann = [1]
    for i in range(1, n):
        john.append((i - ann[john[i-1]]))
        ann.append((i-john[ann[i-1]]))
    return (john, ann)


def john(n):
    return this_kata_is_awful(n)[0]     #Why is the description
    
def ann(n):
    return this_kata_is_awful(n)[1]     #So bad?
    
        
def sum_john(n):
    return sum(john(n))     #It litteraly took me
    
def sum_ann(n):
    return sum(ann(n))     #3 Hours to get what they want