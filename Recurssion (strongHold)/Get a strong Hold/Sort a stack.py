https://www.geeksforgeeks.org/problems/sort-a-stack/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=sort-a-stack

class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):
        # Code here
        
        def sortS(s):
            if len(s) != 0:
                temp = s.pop()
                sortS(s)
                sortIns(s,temp)
        
        def sortIns(s,ele):
            
            if len(s)==0 or s[-1] < ele:
                s.append(ele)
                return
            else:
                temp = s.pop()
                sortIns(s,ele)
                s.append(temp)
        sortS(s)
        return s
