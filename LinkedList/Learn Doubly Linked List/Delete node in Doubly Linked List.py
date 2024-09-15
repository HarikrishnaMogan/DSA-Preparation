https://www.geeksforgeeks.org/problems/delete-node-in-doubly-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=delete-node-in-doubly-linked-list

class Solution:
    def delete_node(self, head, x):
        #code here
        c=0
        temp = head
        b = False
        while temp.next:
            c+=1
            if c==x:
              
                break
            temp=temp.next
            
      
        front = temp.next
        prev = temp.prev
        
        if front==None and prev==None:
            return None
        elif prev == None:
            temp = head
            head = head.next
            head.prev = None
            temp.next = None
            return head
        elif front == None:
            prev.next = None
            temp.prev = None
            return head
        else:
            prev.next = front
            front.prev = prev
            temp.next = None
            temp.prev = None
            return head
        return head
