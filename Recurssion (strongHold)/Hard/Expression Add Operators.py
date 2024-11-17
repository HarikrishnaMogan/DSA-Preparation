https://leetcode.com/problems/expression-add-operators/description/

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res= []
        def dfs(index,curr_res,curr_sum,prev):
            if index >= len(num):
                if curr_sum == target:
                    res.append("".join(curr_res))
                return
            
            for i in range(index, len(num)):

                
                curr_str = num[index:i+1]
                curr_num = int(curr_str)

                if not curr_res:
                    dfs(i+1,[curr_str],curr_num,curr_num)
                else:
                    dfs(i+1,curr_res+["+"]+[curr_str],curr_sum+curr_num,curr_num)
                    dfs(i+1,curr_res+["-"]+[curr_str],curr_sum-curr_num,-curr_num)
                    dfs(i+1,curr_res+["*"]+[curr_str],curr_sum-prev+(curr_num*prev), curr_num*prev)
                #for first time we need zero, for second time this will become leading zero, so we don't want
                if num[index] == "0":
                    break
            
        dfs(0,[],0,0)
        return res
