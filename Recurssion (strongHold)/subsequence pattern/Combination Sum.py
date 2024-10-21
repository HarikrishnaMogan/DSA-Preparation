https://leetcode.com/problems/combination-sum/description/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def combin(i,arr,target,ans,ds):
            if i == len(arr):
                if target == 0:
                    ans.append(ds[:])
                return ans
            
            if arr[i] <= target:
                ds.append(arr[i])
                ans =combin(i,arr,target-arr[i],ans,ds)
                ds.pop()
            
            ans =combin(i+1,arr,target,ans,ds)
            return ans
        return combin(0,candidates,target,[],[])
