
https://www.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=add-1-to-a-number-represented-as-linked-list
   
        def helper(node):
            
            if node == None:
                return 1
            carry = helper(node.next)
            node.data = node.data+carry
            if node.data < 10:
                return 0
            node.data = 0
            return 1
            
            
        
        temp = head
        carry = helper(temp)
        if carry == 1:
            newNode = Node(1)
            newNode.next = temp
            return newNode
        else:
            return head
