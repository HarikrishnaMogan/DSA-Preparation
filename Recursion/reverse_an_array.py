#reversing an array using recursion

arr = [5,4,3,2,1]

def revArr(arr, n ,i):
    if i == n//2:
        return 
    temp = arr[n-i-1]
    arr[n-i-1] = arr[i]
    arr[i] = temp
    revArr(arr, n, i+1)
    return arr

print(revArr(arr,len(arr), 0))
