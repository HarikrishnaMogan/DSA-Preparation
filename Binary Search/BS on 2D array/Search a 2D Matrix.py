https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        low = 0
        high = (n*m)-1
        while low <= high:
            mid = (low+high)//2
            #we can get row and get by dividing and modul by m.
            row = mid//m
            col = mid%m
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid+1
            else:
                high = mid-1
        return False
        
