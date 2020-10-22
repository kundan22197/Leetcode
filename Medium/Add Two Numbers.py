# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, c = 0) -> ListNode:
        val = l1.val + l2.val + c
        c = val // 10
        l = ListNode(val % 10)
        
        if l1.next != None or l2.next != None or c != 0:
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            l.next = self.addTwoNumbers(l1.next, l2.next, c)
        return l
