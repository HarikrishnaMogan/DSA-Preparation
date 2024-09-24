https://www.geeksforgeeks.org/problems/flattening-a-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=flattening-a-linked-list


#User function Template for python3


'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    def flatten(self, root):
        #Your code here
        
        def merge(l1,l2):
            
            dummy=Node(-1)
            res=dummy
            while l1 != None and l2 != None:
                if l1.data < l2.data:
                    res.bottom = l1
                    res=l1
                    l1=l1.bottom
                else:
                    res.bottom = l2
                    res=l2
                    l2=l2.bottom
                res.next = None
                
            #joining remaining list
            if l1:
                res.bottom = l1
            if l2:
                res.bottom = l2
                
            newHead = dummy.bottom
            dummy.bottom = None
            return newHead
            
        def flatSortList(head):
            if head == None or head.next == None:
                return head
                
            mergeHead = flatSortList(head.next)
            return merge(head,mergeHead)
        
        return flatSortList(head)
