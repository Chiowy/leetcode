# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = currunt =  ListNode()
        carry = 0
        value = 0
        
        while carry or l1 or l2:
            val = carry

            if l1: l1, val = l1.next, l1.var + val
            if l2: l2, val = l2.next, l2.var + val

            carry, val = divmod(val, 10)
            currunt.next = currunt = ListNode(val)
        return head.next
