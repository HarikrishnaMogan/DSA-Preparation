https://leetcode.com/problems/kth-missing-positive-number/description/
#brute force
 def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in range(len(arr)):
            if arr[i]<=k: #write and see the logic it correctly represnts the missing number
                k+=1
            else:
                break
        return k
...............................................................

#binary search, optimised approach
def findKthPositive(self, arr: List[int], k: int) -> int:
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            missingNumbers = arr[mid]-(mid+1)#missing = arr[index]-(index+1) #please refer striver video if have doubt
            if missingNumbers <k:
                low=mid+1
            else:
                high=mid-1
        
        #missing = arr[high] - (high+1), more = k-missing
        #ans = arr[high]+more
        #ans = arr[high]+k -(arr[high]-(high+1))
        #ans = arr[high]+k-arr[high]+high+1 
        #ans = k+high+1, if you observer high+1=low
        #so ans = (high+1)+k|| ans=low+k

        return low+k
