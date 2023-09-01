# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        h1, h2 = ListNode(), ListNode()
        t1, t2 = h1, h2
        while head:
            if head.val < x:
                t1.next = head
                t1 = head
            else:
                t2.next = head
                t2 = head
            head = head.next

        t2.next = None
        t1.next = h2.next
        return h1.next
        