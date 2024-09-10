
'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
'''
class Solution:
    def constructLL(self, arr):
        # code here
        head = Node(arr[0])
        mover = head
        for i in range(1,len(arr)):
            temp = Node(arr[i])
            mover.next = temp
            mover=temp
        return head
