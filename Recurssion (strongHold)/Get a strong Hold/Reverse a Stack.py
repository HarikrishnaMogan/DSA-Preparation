https://www.geeksforgeeks.org/problems/reverse-a-stack/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=reverse-a-stack

#User function Template for python3

from typing import List

class Solution:
    def reverse(self,St): 
        #code here
        if len(St) == 0:
            return
        
        temp = St.pop()
        self.reverse(St)
        St.insert(0,temp)
