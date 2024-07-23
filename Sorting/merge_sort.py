# Merge sort (Divide and merge)
# O(nlog(n))

def mergeSort(arr, l, h):
    # l is low, h is high
    if l >= h:      
        return

    mid = (l+h)//2
    # first recursive call to split first half
    mergeSort(arr,l,mid)
    # second revcursive call to split the second half of array
    mergeSort(arr,mid+1, h)
    merge(arr,l,h)
    return arr

def merge(arr,l,h):
    left = l
    mid = (l+h)//2
    right = mid+1
    temp = []
    # sort the elements by checking and pushing in temp array
    while left <= mid and right <= h:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    
    # to append left out elements if any
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right <= h:
        temp.append(arr[right])
        right+=1
    # mapping the sorted element in actual array
    for i in range(l,h+1):
        arr[i] = temp[i-l]


arr1 = [34,1,0,45,2,23,10,98,6,32]

print(mergeSort(arr1,0,len(arr1)-1))

