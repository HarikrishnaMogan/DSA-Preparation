https://www.geeksforgeeks.org/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list
'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    #Function to delete all the occurances of a key from the linked list.
    def deleteAllOccurOfX(self, head, x):
        # code here
        # edit the linked list
        
        #head
        if head == None:
            return head
        if head.next == None:
            if head.data == x:
                return None
            else:
                return head
        
        temp = head
        while temp.next:
        
            if temp.data == x:
                if temp == head: #head
                
                    next = temp.next
                    next.prev = None
                    temp.next = None
                    head = next
                    temp = next
                else:
                    prev = temp.prev
                    next = temp.next
                    prev.next = next
                    next.prev=prev
                    temp.next = None
                    temp.prev = None
                    temp = next
                    
            else:
                temp=temp.next
        #tail
        if temp.data == x:
            prev = temp.prev
            next = temp.next
            prev.next = next
            temp.prev=None
            
        return head
