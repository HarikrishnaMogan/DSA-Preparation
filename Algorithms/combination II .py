

https://leetcode.com/problems/combination-sum-ii/description/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def combin(i,target,arr):
            if target == 0:
                ans.append(ds[:])
                return
            
            for ind in range(i,len(arr)):
                if ind > i and arr[ind] == arr[ind-1]:
                    continue;
                if arr[ind] > target:
                    break;
                
                ds.append(arr[ind])
                combin(ind+1,target-arr[ind],arr)
                ds.pop()
        ans = []
        ds= []
        candidates.sort()
        combin(0,target,candidates)
        return ans
