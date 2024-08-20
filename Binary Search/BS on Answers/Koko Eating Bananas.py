https://leetcode.com/problems/koko-eating-bananas/

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #first find the max inarr
        def findMax(arr):
            maxi = float('-inf')
            for i in range(len(arr)):
                maxi = max(maxi,arr[i])
            return maxi
        
        #calculate the max hours take for selected pile
        def calculateHours(arr,hourly):
            n = len(arr)
            totalHours = 0
            for i in range(n):
                totalHours += math.ceil(arr[i]/hourly)
            return totalHours
        
        #binary search based on max in array
        low=1
        high=findMax(piles)
        ans = float('inf')
        while low<=high:
            m = (low+high)//2
            totalHours = calculateHours(piles,m)
            if totalHours <= h:
                ans = min(ans,m)
                high=m-1
            else:
                low=m+1
        return ans

        
