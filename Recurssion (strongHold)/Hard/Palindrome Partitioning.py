https://leetcode.com/problems/palindrome-partitioning/description/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def part(ind,str,path,ans):
            if ind == len(str):
                ans.append(path[:])
                return
            
            for i in range(ind,len(str)):
                if ispalin(ind,str,i):
                    path.append(str[ind:i+1])
                    part(i+1,str,path,ans)
                    path.pop()
        
        def ispalin(start,str,end):
            while start <= end:
                if str[start] != str[end]:
                    return False
                start+=1
                end-=1
            return True
        ans = []
        path = []
        part(0,s,path,ans)
        return ans
