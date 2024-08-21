
https://takeuforward.org/data-structure/aggressive-cows-detailed-solution/



def cowsPossible(arr,dist,cows):
    c =1
    last = arr[0]
    for i in range(1,len(arr)):
        if arr[i] - last >= dist:
            c+=1
            last=arr[i]
    if c>=cows:
        return True
    else:
        return False

arr = [0, 3, 4, 7, 10, 9]
cows=4
arr.sort()
n = len(arr)
low = 1
high = arr[n-1]-arr[0]
ans = float('-inf')
while low<=high:
    mid = (low+high)//2
    isCows = cowsPossible(arr,mid,cows)
    if isCows:
        ans=mid
        low=mid+1
    else:
        high=mid-1
print(high)
print(ans)
