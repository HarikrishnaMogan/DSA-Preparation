
https://leetcode.com/problems/find-a-peak-element-ii/description/

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        def findMaxIndex(arr,n, col):
            maxi = float('-inf') 
            index = -1
            for i in range(n):
                if maxi < arr[i][col]:
                    maxi = arr[i][col]
                    index = i
            return index
        
        low = 0
        high = len(mat[0])-1
        while low <= high:
            mid = (low+high)//2
            row = findMaxIndex(mat,len(mat),mid)
            left = -1
            if mid-1 >=0:
                left = mat[row][mid-1]

            right = -1
            if mid+1 < len(mat[0]):
                right = mat[row][mid+1]

            if mat[row][mid] > left and mat[row][mid] >right:
                return [row,mid]
            elif mat[row][mid] < left:
                high = mid-1
            else:
                low= mid+1
        return [-1,-1] 
        
        
