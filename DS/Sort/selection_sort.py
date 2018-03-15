def selectionSort(arr):

   for fillslot in range(len(arr)-1,0,-1):
    positionOfMax = 0
    for location in range(1,fillslot+1):
        if arr[location]>arr[positionOfMax]:
            temp = arr[location]
            arr[location] = arr[positionOfMax]
            arr[positionOfMax]=temp
    return arr


arr = [3,4,7,1]
print(selectionSort(arr))


