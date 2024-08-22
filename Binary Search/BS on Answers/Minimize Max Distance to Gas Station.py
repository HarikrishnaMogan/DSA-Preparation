https://takeuforward.org/arrays/minimise-maximum-distance-between-gas-stations/


def countBunks(arr,dist):
    n = len(arr)
    cnt = 0

    for i in range(1,n):
        numbersInbetween = ((arr[i]-arr[i-1])/dist)
        if (arr[i]-arr[i-1]) == (dist * numbersInbetween):
            numbersInbetween-=1
        cnt+=numbersInbetween
    return cnt 





def minimiseMaxdistance(arr,k):
    n =len(arr)
    low =0
    high = 0

    for i in range(n-1):
        high = max(high,arr[i+1]-arr[i])
    
    diff =1e-6

    while high-low > diff:
        mid = (high+low)/2.0
        countofBunks = countBunks(arr,mid)
        if countofBunks > k:
            low = mid
        else:
            high = mid
    return high

arr = [1, 2, 3, 4, 5]
k = 4
ans = minimiseMaxdistance(arr, k)
print("The answer is:", ans)
