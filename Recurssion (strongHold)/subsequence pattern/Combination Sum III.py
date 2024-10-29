
https://leetcode.com/problems/combination-sum-iii/description/
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def comb(i,sum, ans, list,k):
            if sum == 0 and len(list) == k:
                ans.append(list[:])
                return
            if sum < 0 or len(list) > k:
                return
            
            for ind in range(i,10):
                if ind > sum:
                    continue
                list.append(ind)
                comb(ind+1,sum-ind,ans,list,k)
                list.pop()
            return
        
        ans= []
        list = []
        comb(1,n,ans,list,k)
        return ans
