https://leetcode.com/problems/reverse-words-in-a-string/description/

  s=s.strip(" ")
        sr = s.split(" ")
        ans=""
        for i in range(len(sr)-1,-1,-1):
            if sr[i] != "":
                ans+=sr[i]+" "
        return ans.strip(" ")
