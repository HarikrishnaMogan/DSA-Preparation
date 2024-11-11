
https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
from typing import List

class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        # code here
        
        def find(i,j,a,n,ans,s,vis):
            if i == n-1 and j==n-1:
                ans.append(s)
                return
            
            #down
            if(i+1<n and vis[i+1][j]!=1 and a[i+1][j] !=0):
                vis[i][j]=1
                find(i+1,j,a,n,ans,s+'D',vis)
                vis[i][j] = 0
            
            #left
            if(j-1 >=0 and vis[i][j-1]!=1 and a[i][j-1] !=0):
                vis[i][j]=1
                find(i,j-1,a,n,ans,s+'L',vis)
                vis[i][j] = 0
            
            #right
            if(j+1 < n and vis[i][j+1]!=1 and a[i][j+1] !=0):
                vis[i][j]=1
                find(i,j+1,a,n,ans,s+'R',vis)
                vis[i][j] = 0
                
            #up
            if(i-1 >=0 and vis[i-1][j]!=1 and a[i-1][j]!=0):
                vis[i][j]=1
                find(i-1,j,a,n,ans,s+'U',vis)
                vis[i][j] = 0
                
        
        ans=[]
        if m[0][0] == 0:
            ans.append("-1")
            return ans
        
        n = len(m)
        vis = [[0 for _ in range(n)] for _ in range(n)]
        
        find(0,0,m,n,ans,"",vis)
        
        if len(ans) == 0:
            ans.append("-1")
        return ans
