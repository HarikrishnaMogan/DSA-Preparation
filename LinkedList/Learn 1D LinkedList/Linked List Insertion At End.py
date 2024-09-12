https://www.geeksforgeeks.org/problems/linked-list-insertion-1587115620/0?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=linked-list-insertion

'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        # code here 
        if head == None:
            return Node(x)
        temp = head
        while temp.next:
            temp=temp.next
        k = Node(x)
        temp.next = k
        return head
