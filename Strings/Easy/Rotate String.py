https://leetcode.com/problems/rotate-string/description/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        elif s==goal:
            return True
        last = len(goal)-1
        for i in range(len(goal)):
            goal = goal[last:]+goal[:last]
            if s==goal:
                return True
        return False

................................................

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        elif s==goal:
            return True
        temp = s+s
        if goal in temp:
            return True
        else:
            return False
