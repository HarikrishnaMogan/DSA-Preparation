https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=number-of-occurrence


#User function Template for python3
class Solution:

	def count(self,arr, n, x):
		# code here
		#first occurance
		l = 0
		h = n-1
		first = -1
		while l<=h:
		    m = (l+h)//2
		    if arr[m] == x:
		        first = m
		        h=m-1
		    elif arr[m] < x:
		        l=m+1
		    else:
		        h=m-1
		 #last occurance
		last = -1
		l=0
		h=n-1
		while l <=h:
		    m=(l+h)//2
		    if arr[m] ==x:
		        last =m
		        l=m+1
		    elif arr[m] < x:
		        l=m+1
		    else:
		        h=m-1
		
	    if first !=-1:
	        return last-first+1 #count the occurances
	    else:
	        return 0
