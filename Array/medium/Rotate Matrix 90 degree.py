https://leetcode.com/problems/rotate-image/description/

class Solution(object):
    def rotate(self, matrix):
      
        # first transpose the matrix, (rows will become columns, columns become rows)
        # second reverse each row of transposed matrix

#transposing the matrix
#iterating only righthalf of the diagonal, since diagonal no need for swap, with this righthalf itself we can transpoe the matrix by swapping
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[i])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

#reversing the each row of transposed matrix
        for i in range(len(matrix)):
            k = 0
            l =len(matrix[i])-1
            while k < l:
                temp = matrix[i][k]
                matrix[i][k] = matrix[i][l]
                matrix[i][l] = temp
                k+=1
                l-=1
        return matrix 
                

                
