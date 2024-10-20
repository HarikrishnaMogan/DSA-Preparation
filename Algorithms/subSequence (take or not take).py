



https://leetcode.com/problems/subsets/description/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def subseq(i,curr,ans,nums,n):
            if n == i:
                ans.append(curr[:])
                return ans
            
            curr.append(nums[i])
            ans =subseq(i+1,curr,ans,nums,n)
            curr.pop()
            ans =subseq(i+1,curr,ans,nums,n)
            return ans
        ans = []
        curr = []
        return subseq(0,curr,ans,nums,len(nums))
