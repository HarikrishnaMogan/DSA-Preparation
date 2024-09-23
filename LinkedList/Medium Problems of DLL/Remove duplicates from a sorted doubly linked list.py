https://www.geeksforgeeks.org/problems/remove-duplicates-from-a-sorted-doubly-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=remove-duplicates-from-a-sorted-doubly-linked-list

class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        if head==None:
            return head
        temp = head.next
        while temp:
            prev = temp.prev
            next = temp.next
            
            if prev.data == temp.data or (next and temp.data == next.data):
                prev.next = next
                next.prev = prev
                temp.next=None
                temp.prev=None
                temp = next
            else:
                temp=temp.next
        return head
                
