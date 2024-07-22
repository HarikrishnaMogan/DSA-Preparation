# Insertion sort (take an element and place it in its correct order )
# compare current element with previous element and swap if smaller, till all elements on the left is sorted
# best case O(N), worst case O(N^2)

def insertionSort(arr):
    n = len(arr)
    for i in range(n):
        j = i
        
        while j > 0 and arr[j-1] > arr[j]:
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j-=1
    return arr

sortedArr = insertionSort([23,0,5,1,43,20,19,8,3])
print(sortedArr)
