https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/


 l =0 
        h=len(nums)-1
        ans = float('inf')
        while l<=h:
            m = (l+h)//2

            if nums[l]<=nums[h]: #if this happens then the entrie part is sorted no need for searching
                ans = min(ans,nums[l])
                break;
            #here low is the min, since it is sorted part
            if nums[l]<=nums[m]:
                ans=min(ans,nums[l])
                l=m+1
            #here mid is the min, since mid to high is sorted part
            else:
                ans=min(ans,nums[m])
                h=m-1
        return ans
