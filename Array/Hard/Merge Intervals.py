
#https://leetcode.com/problems/merge-intervals/description/
  intervals.sort()
        ans = []
        for i in range(len(intervals)):
            if len(ans) == 0 or ans[len(ans)-1][1] < intervals[i][0]: #check last element of ans and first element of intervals to verify if it overlaps
                ans.append(intervals[i])
            else:
                ans[len(ans)-1][1] = max(ans[len(ans)-1][1],intervals[i][1]) #if overlap update the max value at end
        return ans
.........................................................
  intervals.sort()
        ans = []
        for i in range(len(intervals)):
            if not ans or ans[-1][1] < intervals[i][0]:
                ans.append(intervals[i])
            else:
                ans[-1][1] =  max(ans[-1][1], intervals[i][1])
        return ans
