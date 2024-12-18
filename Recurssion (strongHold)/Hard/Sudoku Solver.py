https://leetcode.com/problems/sudoku-solver/description/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(board,row,col,c):
            for i in range(9):
                if board[row][i] == c:
                    return False
                if board[i][col] == c:
                    return False
                if board[3*(row//3)+i//3][3*(col//3)+i%3] == c:
                    return False
            return True


        def solve(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == ".":
                        for c in "123456789":
                            if isValid(board,i,j,c) == True:
                                board[i][j] = c
                                if solve(board) == True:
                                    return True
                                else:
                                    board[i][j] = "."
                        return False
            return True

        solve(board)
        return board
