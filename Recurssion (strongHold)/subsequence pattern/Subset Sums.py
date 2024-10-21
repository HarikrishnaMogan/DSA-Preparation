
https://www.geeksforgeeks.org/problems/subset-sums2234/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=subset-sums

#User function Template for python3
class Solution:
	def subsetSums(self, arr, n):
		# code here
		def subsetsum(i,arr,sum):
		    if i == len(arr):
		        ans.append(sum)
		        return
		    sum += arr[i]
		    subsetsum(i+1,arr,sum)
		    sum-=arr[i]
		    subsetsum(i+1,arr,sum)
	    
	    ans = []
	    subsetsum(0,arr,0)
	    return ans
