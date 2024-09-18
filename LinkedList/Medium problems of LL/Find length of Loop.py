https://www.geeksforgeeks.org/problems/find-length-of-loop/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find-length-of-loop

#User function Template for python3

'''
Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        #Your code here
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow=slow.next
            fast = fast.next.next
            if slow == fast:
                fast = fast.next
                c=1
                while slow != fast:
                    fast=fast.next
                    c+=1
                return c
        return 0
