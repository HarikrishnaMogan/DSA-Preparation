
#https://practice.geeksforgeeks.org/problems/count-digits5716/1



    def evenlyDivides (self, N):
        # code here
        cnt = 0
        k = N
        while k > 0:
            
            d = k%10
            if d != 0 and N%d == 0:
                cnt = cnt + 1
            k = k//10
        
        return cnt