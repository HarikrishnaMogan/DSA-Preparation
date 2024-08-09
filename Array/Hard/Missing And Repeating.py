https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find-missing-and-repeating

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        #sum of N natural numbers, sn = n*(n+1)/2
        #sum of square of N natural num, s2n = n*(n+1)*(2n+1)/6
        #x-y =s1-sn (val1)
        #x^2-y^2 = s2-s2n (a^2-b^2 = (a+b)(a-b))
        #(x+y)(x-y) = s2-s2n
        #x+y = s2-s2n/(x-y) (val2)
        #now we have two equations to solve as aper alzebgra
        #upon solving we get, 2x = val1+val2 => x =(val2+val2)/2
        
        s1 =0
        s2=0
        sn = (n*(n+1))//2
        s2n = (n*(n+1)*(2*n+1))//6
        
        for i in arr:
            s1+=i
            s2+= i*i
        
        val1 = s1-sn
        val2 = s2-s2n
        val2 = val2/val1  #x+y = s2-s2n/(x-y)
        x = int((val1+val2)//2) #2x = val1+val2 => x =(val2+val2)/2
        y = int(x - val1)
        return [x,y]
        
