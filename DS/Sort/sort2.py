def quick_sort(arr):
    quick_sort_helper(arr,0,len(arr)-1)
    return arr

def quick_sort_helper(arr,first,last):

    if first<last:
        splitpoint = partition(arr,first,last)
        quick_sort_helper(arr,first,splitpoint-1)
        quick_sort_helper(arr,splitpoint+1,last)

def partition(arr,first,last):
    pivot = arr[first]
    leftmark = first +1
    rightmark = last

    done = False

    while not done:
        while leftmark <= rightmark and arr[leftmark]<= pivot:
            leftmark = leftmark +1

        while rightmark >=leftmark and arr[rightmark] >=pivot:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark]=arr[rightmark]
            arr[rightmark]=temp
    temp = arr[first]
    arr[first]=arr[rightmark]
    arr[rightmark]=temp
    return rightmark

print(quick_sort([3,6,1,7,9,2]))
