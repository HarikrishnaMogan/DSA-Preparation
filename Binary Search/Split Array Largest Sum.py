https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def getSplitCount(arr,maxi,split):
            count = 1
            sum =0
            for i in range(len(arr)):
                if sum+arr[i] <= maxi:
                    sum+=arr[i]
                else:
                    sum=arr[i]
                    count+=1
            return count




        if(len(nums)) < k:
            return -1
        low = max(nums)
        high = sum(nums)
        while low<=high:
            mid=(low+high)//2
            splitCount = getSplitCount(nums,mid,k)
            if splitCount > k:
                low = mid+1
            else:
                high = mid-1
        return low
