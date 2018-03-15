# works on ordered arr/list

def seq_search(arr,ele):
    found = False
    stopped = False
    pos = 0
    while pos <len(arr) and not found and not stopped:
        if arr[pos] == ele:
            found = True
        elif arr[pos]> ele:
            stopped = True
        else:
            pos += 1

    return found

arr = [1,2,3,4]

print(seq_search(arr,5))
