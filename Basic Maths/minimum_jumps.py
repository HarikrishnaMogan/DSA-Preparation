https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1

#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
	    #code here
	    if n <= 1:
	        return 0
	        
	    if arr[0] == 0:
	        return -1
	        
	  
	    maxReach = arr[0] # initialize maxreach,step,jump
	    step =  arr[0]
	    jump = 1
	    
	    
	    for i in range(1, n):
	        
	        if i == n-1: #if i equal to length then we reached the end
	            return jump
	           
	        maxReach = max(maxReach , i+arr[i]) #count the maxreach by adding array index so that we get the end of the reach of array
	        step -= 1
	        
	        if step == 0:
	            if i >= maxReach: #if arr[i] values becomes 0 or less than 0 ,in those cases, i shoould be >= maxReach
	                return -1
	                
	            jump += 1
	            step = maxReach - i #-i to get the step, since we added i in previous steps
	    return -1
	
	            
	        
