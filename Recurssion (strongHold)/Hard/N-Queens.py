https://leetcode.com/problems/n-queens/description/



class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def solve(col,board,ans,n,leftrow,lowerDiagonal,upperDiagonal):
            if col == n:
                ans.append(board[:])
                return
            
            for row in range(n):
                if leftrow[row] == 0 and lowerDiagonal[col+row]==0 and upperDiagonal[n-1+col-row]==0:
                    board[row] = board[row][:col]+'Q'+board[row][col+1:]
                    leftrow[row]=1
                    lowerDiagonal[col+row]=1
                    upperDiagonal[n-1+col-row]=1
                    solve(col+1,board,ans,n,leftrow,lowerDiagonal,upperDiagonal)
                    board[row] = board[row][:col]+'.'+board[row][col+1:]
                    leftrow[row]=0
                    lowerDiagonal[col+row]=0
                    upperDiagonal[n-1+col-row]=0
        
        ans=[]
        leftrow = [0]*n
        lowerDiagonal = [0]*(2*n-1)
        upperDiagonal = [0]*(2*n-1)
        board = ['.'*n for i in range(n)]
        solve(0,board,ans,n,leftrow,lowerDiagonal,upperDiagonal)
        return ans
