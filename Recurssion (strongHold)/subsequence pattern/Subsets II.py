https://leetcode.com/problems/subsets-ii/description/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def subset(i,nums,ds,ans):
            ans.append(ds[:])

            for ind in range(i,len(nums)):
                if i != ind and nums[ind] == nums[ind-1]:
                    continue
                ds.append(nums[ind])
                subset(ind+1,nums,ds,ans)
                ds.pop()
            return ans
        nums.sort()
        return subset(0,nums,[],[])
