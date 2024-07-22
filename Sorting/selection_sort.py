#selection sort (select and element then swap)
#step 1: select an element
#step2: find the minimum and swap

def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        mini = i
        for j in range(i,n):
            if arr[mini] > arr[j]:
                mini = j
        temp = arr[mini]
        arr[mini] = arr[i]
        arr[i] = temp
    return arr


sortedArr = selectionSort([43,21,67,13,0,9,4])
print(sortedArr)

