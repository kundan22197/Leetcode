# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        def length(head):
            l = 0
            temp = head
            while temp:
                temp = temp.next
                l += 1
            return l
        
        def rev(head, k):
            curr = head
            nex = None
            prev = None
            count = 0
        
            while curr is not None and count < k:
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex
                count += 1
                
            if nex is not None:

                if length(nex) >= k:
                    head.next = rev(nex, k)

                else:
                    head.next = nex
                    nex = nex.next
                    head = head.next

            return prev
        
        head = rev(head, k)
        return head
            
        
    
            
            
    
 

        
            
            
              
        