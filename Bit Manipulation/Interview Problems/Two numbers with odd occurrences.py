https://www.geeksforgeeks.org/problems/two-numbers-with-odd-occurrences5846/1

def twoOddNum(self, Arr, N):
        # code here
        xor=0
        
        for i in Arr:
            xor^=i
            
            
        rightmostBit = (xor & xor-1) ^ xor
        
        b1=0
        b2=0
        
        for i in Arr:
            if i & rightmostBit:
                b1=b1^i
            else:
                b2=b2^i
                
        if b1 > b2:
            return [b1,b2]
        else:
            return [b2,b1]
            
