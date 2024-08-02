https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        col0 =1
        #use first row , column for marking zero, based on marking we will set other elements
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 =0

#based on first row matrix[i][0] and column matrix [0][j], changing the other elements to zero,
#we should start from matrix[1][1],then only the mapping will not overwritten
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][0] == 0 or matrix[0][j]==0:
                    matrix[i][j] = 0
  #Now start chnaging the first row, matrix[0][j]      
        for j in range(len(matrix[0])):
            if matrix[0][0] == 0:
                matrix[0][j] = 0
 #now start chnaging the first column , matrix[i][0]       
        for i in range(len(matrix)):
            if col0 == 0:
                matrix[i][0] = 0
        
        return matrix
                    
