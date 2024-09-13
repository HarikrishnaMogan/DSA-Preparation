https://www.geeksforgeeks.org/problems/introduction-to-doubly-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=introduction-to-doubly-linked-list

# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    def constructDLL(self, arr):
        # Code here
        head = Node(arr[0])
        prev = head
        for i in range(1,len(arr)):
            temp = Node(arr[i])
            temp.prev = prev
            prev.next = temp
            prev = temp
        return head
