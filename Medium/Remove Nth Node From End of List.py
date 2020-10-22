# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None:
            return head
        temp = head
        l = 1
        while temp.next != None:
            temp = temp.next
            l += 1
        temp = head
        if l == n:
            head = head.next
            return head
        for i in range(l-n-1):
            temp = temp.next
        temp.next = temp.next.next
        return head
            
            