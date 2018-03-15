def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for n in range(i):
            if arr[n]>arr[n+1]:
                temp = arr[n]
                arr[n]=arr[n+1]
                arr[n+1]=temp
    return arr



print(bubble_sort([3,6,1,7,9,2]))


def selection_sort(arr):

    for i in range(0,len(arr)):
        min = i
        for y in range(i,len(arr)):
            if arr[min]>arr[y]:
                temp = arr[min]
                arr[min]=arr[y]
                arr[y]=temp
    return arr

print(selection_sort([3,6,1,7,9,2]))

def insertion_sort(arr):

    for i in range(1,len(arr)):
        j = i
        toInsert = arr[i]
        while((j>0) and (arr[j-1]>toInsert)):
            arr[j]=arr[j-1]
            j = j-1
        arr[j]=toInsert

    return arr

print(insertion_sort([3,6,1,7,9,2]))






