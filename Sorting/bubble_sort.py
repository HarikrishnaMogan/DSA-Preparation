# Bubble sort (push the max element to last by adjacent swaps)
# step1: compare current and next element
# step2: swap the largest element to last

def bubbleSort(arr):
    n = len(arr)
    for i in range(n,0,-1):
        for j in range(0,i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    return arr

sortedArr = bubbleSort([23,0,5,1,43,20,19,8,3])
print(sortedArr)
