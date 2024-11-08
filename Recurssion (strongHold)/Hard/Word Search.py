
https://leetcode.com/problems/word-search/
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def check(board,word,i,j,k):
            if k == len(word):
                return True
            
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[k] != board[i][j]:
                return False
            
            temp =board[i][j]
            board[i][j] = ""

            #going up, down, right,left
            ans = (check(board,word,i+1,j,k+1) or 
                    check(board,word,i-1,j,k+1) or
                    check(board,word,i,j+1,k+1) or
                    check(board,word,i,j-1,k+1))
            #restore value
            board[i][j] = temp

            return ans
        
        #check for the word starting point and start from there
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] ==word[0]:
                    if check(board,word,i,j,0)==True:
                        return True
        return False
