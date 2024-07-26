
https://leetcode.com/problems/max-consecutive-ones/description/
     sum = 0
        m = 0
        for i in nums:
            if i == 1:
                sum+=1
            else:
                m = max(m,sum)
                sum =0
        m = max(m,sum)
        return m
