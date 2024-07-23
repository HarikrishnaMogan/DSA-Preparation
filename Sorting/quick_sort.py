# quick sort (Divide and Conquer)
# step 1: take a pivot and place it in its correct position
# step2: smaller elements to the left and larger to the right of the pivot
# Tc = O(Nlog(N)), sc = O(1)


def quickSort(arr,l,h):
    # if l = h there will be only one element, thats why l < h
    if l < h:
        # place the pivot and swap small to left and large to right
        partionIndex = PlacePivot(arr, l ,h)
        quickSort(arr, l, partionIndex-1)
        quickSort(arr,partionIndex+1, h)
        return arr

def PlacePivot(arr, l, h):
    i = l
    j = h
    pivot = l

# check for i < j
    while i < j:

# find if an element is larger than pivot from the left
        while arr[i] <= arr[pivot] and i <= h-1:
            i+=1
# find if an element is smaller than pivot  from the right
        while arr[j] > arr[pivot] and j >= l+1:
            j-=1
# once found both swap
        if i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    # finally place pivot in its correct place by swapping and return partion index for next recursion
    temp =  arr[pivot]
    arr[pivot] = arr[j]
    arr[j] = temp
    return j 
        





arr1 = [34,1,0,45,2,23,10,98,6,32]

print(quickSort(arr1,0,len(arr1)-1))

