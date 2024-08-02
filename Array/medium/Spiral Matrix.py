
https://leetcode.com/problems/spiral-matrix/description/

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        left = 0
        right = len(matrix[0])-1
        top = 0
        bottom = len(matrix)-1
        ans = []

        while top <= bottom and left <= right:

            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top+=1

            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right-=1

            if top <= bottom: #to handle single line array
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
            bottom-=1

            if left <= right:
                for i in range(bottom, top-1,-1):
                    ans.append(matrix[i][left])
            left+=1
        return ans
