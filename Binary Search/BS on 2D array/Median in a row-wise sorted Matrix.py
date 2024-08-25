https://www.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=median-in-a-row-wise-sorted-matrix
class Solution:
    def median(self, matrix, R, C):
    	#code here 
    	def upperbound(arr,x):
    	    low =0
    	    high = len(arr)-1
    	    ans = len(arr)
    	    while low<=high:
    	        mid=(low+high)//2
    	        if arr[mid] > x:
    	            high=mid-1
    	            ans=mid
    	        else:
    	            low=mid+1
    	    return ans
    	    
        def smallEqual(mat,x):
            cnt=0
            for i in range(len(mat)):
                cnt+= upperbound(mat[i],x)
            return cnt
        low =float('inf')
        high=float('-inf')
        req = (R*C)//2
        for i in range(len(matrix)):
            low = min(low,matrix[i][0])
            high = max(high,matrix[i][C-1])
        
        while low<=high:
            mid = (low+high)//2
            smallEq = smallEqual(matrix,mid)
            if smallEq <= req:
                low=mid+1
            else:
                high = mid-1
        return low
                
            
                
