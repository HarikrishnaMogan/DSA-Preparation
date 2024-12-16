https://www.geeksforgeeks.org/problems/prime-factors5052/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=Prime-Factors

	def AllPrimeFactors(self, N):
		# Code here
		list = []
		i=2
		while i*i <= N:
		    if N%i==0:
		        list.append(i)
		        
		        while N%i==0:
		            N=N//i
		    i+=1
        if N != 1:
            list.append(N)
        return list
