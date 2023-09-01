# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        fast = slow = head
        for i in range(n):
            fast = fast.next

        prev = None
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next

        if prev:
            prev.next = slow.next
            slow.next = None
            return head
        return slow.next