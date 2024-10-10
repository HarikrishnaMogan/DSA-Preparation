class Solution:
    def myAtoi(self, s: str) -> int:
    



      
        def atoi(s,ans,i):
            if i >=len(s):
                return ans
            if not s[i].isnumeric():
                if (s[i]=="-" or s[i]=="+") and i ==0:
                    ans=s[i]
                    if s[i] == "+":
                        ans= None
                else:
                    return ans
            if s[i].isnumeric():
                if ans:
                    ans+=s[i]
                else:
                    ans=s[i]
            i+=1
            return atoi(s,ans,i)
        s = s.strip()
        ans = atoi(s,None,0)
            
            

        if ans==None or ans== "-":
            return 0
        elif (int(ans)) < -2**31:
            return -2**31
        elif (int(ans)) > 2**31-1:
            return 2**31-1
        else:
            return int(ans)

            
