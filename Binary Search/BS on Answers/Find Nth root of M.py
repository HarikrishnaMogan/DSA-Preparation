https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find-nth-root-of-m


	def NthRoot(self, n, m):
		# Code here
		l =1
		h = m
		while l<=h:
		    mid=(l+h)//2
		    x = mid**n
		    if x == m:
		        return mid
		        
            if x < m:
                l=mid+1
            else:
                h=mid-1
        return -1
