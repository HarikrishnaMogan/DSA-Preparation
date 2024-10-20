https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=perfect-sum-problem

class Solution:
	def perfectSum(self, arr, n, sum):
		# code here
		
		def subseqcount(i,k,arr,n,sum):
		    count =0
		    if i == n:
		        if sum == k:
		            return 1
		        return 0
		    
		    k+=arr[i]
		    count+=subseqcount(i+1,k,arr,n,sum)
		    k-=arr[i]
		    count+= subseqcount(i+1,k,arr,n,sum)
		    return count
        return subseqcount(0,0,arr,n,sum)

#.......................................................................

#User function Template for python3
class Solution:
	def perfectSum(self, arr, n, sum):
		# code here
		
		def subseqcount(i,k,arr,n,sum):
		  
		    if i == n:
		        if sum == k:
		            return 1
		        return 0
		    
		    k+=arr[i]
		    l=subseqcount(i+1,k,arr,n,sum)
		    k-=arr[i]
		    r= subseqcount(i+1,k,arr,n,sum)
		    return l+r
        return subseqcount(0,0,arr,n,sum)
