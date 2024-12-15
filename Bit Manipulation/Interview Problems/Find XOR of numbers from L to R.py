https://www.geeksforgeeks.org/problems/find-xor-of-numbers-from-l-to-r/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find-xor-of-numbers-from-l-to-r

    def findXOR(self, l, r):
        # Code here
        
        def findxor(n):
            k = n%4
            if k == 1:
                return 1
            if k == 2:
                return n+1
            if k == 3:
                return 0
            if k ==0:
                return n
        
        return findxor(l-1) ^ findxor(r)
