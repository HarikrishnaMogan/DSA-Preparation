https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=reverse-a-doubly-linked-list

#User function Template for python3

'''
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def reverseDLL(self, head):
        #return head of reverse doubly linked list
        if head == None or head.next == None:
            return head
        prev = None
        current = head
        while current:
            prev = current.prev
            current.prev = current.next
            current.next = prev
            current=current.prev
        return prev.prev
