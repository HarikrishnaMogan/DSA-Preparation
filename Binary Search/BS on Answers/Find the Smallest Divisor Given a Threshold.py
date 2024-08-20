https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def findMax(arr):
            maxi = float('-inf')
            for i in range(len(arr)):
                maxi = max(maxi,arr[i])
            return maxi
        
        def computeThreshold(arr,divisor):
            thres = 0
            for i in range(len(arr)):
                thres +=math.ceil(arr[i]/divisor)
            return thres
        
        low =1
        high=findMax(nums)
        ans=1
        while low <=high:
            mid = (low+high)//2
            thres = computeThreshold(nums,mid)
            if thres <= threshold:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
