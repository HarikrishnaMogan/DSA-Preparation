https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

l = 0
        h= len(nums)-1
        while l<=h:
            m = (l+h)//2

            if nums[m] == target:
                return True
            if nums[l] == nums[m] and nums[m] == nums[h]: #added this condition to tackle duplicates, if true we need to srink the search space
                l=l+1
                h=h-1
                continue
            if nums[l]<=nums[m]:
                if nums[l]<=target and target<=nums[m]:
                    h=m-1
                else:
                    l=m+1
            else:
                if nums[m]<=target and target <= nums[h]:
                    l=m+1
                else:
                    h=m-1
        return False
