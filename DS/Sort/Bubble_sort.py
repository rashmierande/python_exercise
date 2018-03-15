def bubble_sort(arr):
    for n in range(len(arr)-1,0,-1):
        for k in range(n):
            if arr[k]>arr[k+1]:
                temp = arr[k]
                arr[k]=arr[k+1]
                arr[k+1]=temp
    return arr

arr = [5,3,7,2]
print(bubble_sort(arr))


def bubble_sort_desc(arr):
    for n in range(0,len(arr),1):
        for k in range(n):

            if arr[k]<arr[k+1]:
                temp = arr[k]
                arr[k]=arr[k+1]
                arr[k+1]=temp
    return arr

arr = [5,3,7,2]
print(bubble_sort_desc(arr))