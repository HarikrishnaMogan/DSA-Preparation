

https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/

    def minBitFlips(self, start: int, goal: int) -> int:
        ans = start ^ goal
        cnt=0
        for i in range(31):
            if ans & 1<<i:
                cnt+=1
        return cnt