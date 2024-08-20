https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def findMaxMin(arr):
            mini =float('inf')
            maxi = float('-inf')
            for i in range(len(arr)):
                mini = min(mini,arr[i])
                maxi = max(maxi,arr[i])
            return [mini,maxi]

        #checking if the get the number of boques or not
        def possible(arr,day,m,k):
            count=0
            boquey = 0
            for i in range(len(arr)):
                #since only adjacent flowers should be used, making the counter as zero if there any flower doesnt bloom,so that will be able to calculate the correct no of boques
                if arr[i] <= day:
                    count+=1
                else:
                    boquey += count//k
                    count=0 
            boquey += count//k
            if boquey >= m:
                return True
            else:
                return False
        #if m*k > number of flowers in array, it is not possible to form boques
        if len(bloomDay) < m*k:
            return -1
        
        miniMax = findMaxMin(bloomDay)
        low = miniMax[0]
        high = miniMax[1]
        ans= float('inf')
        while low <= high:
            mid = (low+high)//2
            poss = possible(bloomDay,mid,m,k)
            #if possible is true, we want minimum days, so high=mid-1
            if poss:
                ans=mid
                high=mid-1
            #if possible is False, we want possible so negelect the part not possible, so low=mid+1
            else:
                low = mid+1
        return ans

        
