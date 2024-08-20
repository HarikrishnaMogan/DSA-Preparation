https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def findMaxWeight(arr):
            maxi = 0
            for i in range(len(arr)):
                maxi += arr[i]
            return maxi

        def countDays(arr,cap):
            day=1
            load=0
            for i in range(len(arr)):
                if load+arr[i] > cap:
                    day+=1
                    load = arr[i]
                else:
                    load+=arr[i]
            return day
        

        low =max(weights) #low should be max of arr(weights),otherwise we cant solve because we can't ship that weight logically if we take low as 1
        high = findMaxWeight(weights) #sum of all weights
        ans = float('inf')
        while low<=high:
            mid=(low+high)//2
            noOfDays = countDays(weights,mid)
            if noOfDays <= days:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
