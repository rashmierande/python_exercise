def insertionSort(arr):

    for i in range(1,len(arr)):
        curVal = arr[i]
        position = i
        while position > 0 and arr[position - 1] > curVal:
            # print(arr[position] , " -> ", arr[position -1])
            arr[position] = arr[position -1]
            position = position -1
        arr[position] = curVal

    return arr

arr = [4,6,1,9,0,2]
print(insertionSort(arr))