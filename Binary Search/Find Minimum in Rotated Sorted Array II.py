https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

        low=0
        high=len(nums)-1
        ans = float('inf')
        while low<=high:
            mid=(low+high)//2
            if nums[low] == nums[mid] and nums[mid]==nums[high]: #to handle duplicate values
                if nums[low]<ans:
                    ans=nums[low]
                low+=1
                high-=1
                continue

            if nums[low]<=nums[mid]:
                if nums[low]<ans:
                    ans=nums[low]
                low=mid+1
            else:
                if nums[mid]<ans:
                    ans=nums[mid]
                high=mid-1
        return ans

.............................................
#if index asked

nums = [2,2,2,0,1]

low=0
high=len(nums)-1
ans = float('inf')
index=-1
while low<=high:
    mid=(low+high)//2
    if nums[low] == nums[mid] and nums[mid]==nums[high]:
        if nums[low] < ans:
            ans=nums[low]
            index=low
        low+=1
        high-=1
        continue

    if nums[low] <= nums[mid]:
        if nums[low] < ans:
            ans=nums[low]
            index=low
        low=mid+1
    else:
        if nums[mid] < ans:
            ans=nums[mid]
            index=low
        high=mid-1
print(ans,index)
        
