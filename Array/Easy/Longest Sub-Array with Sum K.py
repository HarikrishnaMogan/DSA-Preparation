
https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=longest-sub-array-with-sum-k
# this sol works for both positive and negative numbers
# TC -> O(N), SC-> O(N)

    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        map ={}
        sum = 0
        i =0
        maxLen = 0
        while i < n:
            sum+=arr[i]
            
            if sum == k:
                maxLen = max(maxLen,i+1)
                
            #check reminder is present in map   
            rem = sum-k
            if rem in map:
                len = i - map[rem]
                maxLen = max(maxLen,len)
            
            #do not update index in map if sum already present, then only it will handle negative and zeros
            if sum not in map:
                map[sum] = i
            i+=1
                
        return  maxLen
..................................................................................................................
# this will only work for positive numbers
# sliding window
# TC -> O(N), SC-> O(1)
def maxLenArr(arr , k):
    i= 0
    j =0
    sum =0
    maxLen = 0
    while j < len(arr):
        sum+=arr[j]

        while sum > k and i <= j:
            sum-=arr[i]
            i+=1
    
        if sum == k:
            maxLen = max(maxLen, j-i+1)
        j+=1
    return maxLen
            
