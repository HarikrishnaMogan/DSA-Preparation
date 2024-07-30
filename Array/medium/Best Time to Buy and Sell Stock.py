
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
 p = 0
        ele = prices[0]
        for i in prices:
            if i <=ele:
                ele = i
            else:
                pr =  i-ele
                p = max(p,pr)
        return p
............................................
# using two pointer
 i = 0
        j = 1
        pr = 0
        while j < len(prices):
            p = prices[i] - prices[j]
            if p > 0:
                i = j
                j+=1
            else:
                pr = max(pr, abs(p))
                j+=1
        return pr
