# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        t = head
        length = 0
        while t != None:
            length += 1
            t = t.next
        if length in [0,1]:
            return head
        if length%2 != 0:
            l1 = head
            l2 = l1.next
            l1.next = l2.next
            l2.next = l1
            head = l2
            temp = l1
            while temp.next.next != None:
                l1 = temp.next
                l2 = l1.next
                l1.next = l2.next
                l2.next = l1
                temp.next = l2
                temp = temp.next.next
            return head
        l1 = head
        l2 = l1.next
        l1.next = l2.next
        l2.next = l1
        head = l2
        temp = l1
        if l1.next == None:
            return head
        while temp.next.next.next != None:
            l1 = temp.next
            l2 = l1.next
            l1.next = l2.next
            l2.next = l1
            temp.next = l2
            temp = temp.next.next
        else:
            l1 = temp.next
            l2 = l1.next
            temp.next = l2
            l2.next = l1
            l1.next = None
        return head

            
        
        