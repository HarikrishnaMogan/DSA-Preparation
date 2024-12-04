https://www.geeksforgeeks.org/problems/check-whether-k-th-bit-is-set-or-not-1587115620/1

    #Function to check if Kth bit is set or not.
    def checkKthBit(self, n,k):
        #Your code here
        bits = ""
        while n >=1:
            if n%2==0:
                bits+="0"
            else:
                bits+="1"
            n = n//2
        remLen = "0"*(32-len(bits))
        bits = bits+remLen
        if bits[k] == "1":
            return True
        return False
