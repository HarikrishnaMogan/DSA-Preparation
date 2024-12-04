
https://www.geeksforgeeks.org/problems/bit-manipulation-1666686020/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=bit-manipulation
class Solution:
    def bitManipulation(self, num, i):
        # Code here
        bits = ""
        ans = []
        while num >= 1:
            if num%2 == 0:
                bits+="0"
            else:
                bits+="1"
            num = num//2
        #to append remanings bits for 32 bits
        remlen = "0"*(32-len(bits))
        bits = bits+remlen
        #reversing the bits
        bits = bits[::-1]
        ith = len(bits)-i
        
        ans.append(int(bits[ith]))
        #set and clear bits
        ans.append(0)
        ans.append(0)
        
        p=1
        for j in range(len(bits)-1,-1,-1):
            if bits[j] == "1" or ith == j:
                if ith == j: #set the bit only for ans[1]
                    ans[1] = ans[1]+p
                else: 
                     ans[1] = ans[1]+p
                     ans[2] = ans[2]+p
                    
            p = p*2
        print(str(ans[0])+" "+str(ans[1])+" "+str(ans[2]))
                
            
        
        
