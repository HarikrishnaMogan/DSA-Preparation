https://www.geeksforgeeks.org/problems/count-number-of-substrings4528/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=count-number-of-substrings

#User function Template for python3

class Solution:
    def substrCount (self,s, k):
        # your code here
        if len(s) == 0:
            return 0
            
        def countSubK(st,t):
            map={}
            l=0
            i=0
            nums=0
            while i < len(st):
                if st[i] in map:
                    map[st[i]]+=1
                else:
                    map[st[i]] = 1
                    
                while len(map) > t:
                    map[st[l]]-=1
                    if map[st[l]]==0:
                        map.pop(st[l])
                    l+=1
                
                nums += i-l+1
                i+=1
            return nums
        
        return countSubK(s,k)-countSubK(s,k-1)
                    
