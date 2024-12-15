https://leetcode.com/problems/subsets/description/


 def subsets(self, nums: List[int]) -> List[List[int]]:

       subset = 2**len(nums)
       ans=[]
       for i in range(subset):
        list = []
        for j in range(len(nums)):
            if i & 1<<j:
                list.append(nums[j])
        ans.append(list[:])
       return ans
       
