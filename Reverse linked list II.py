# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left_node, right_node = head, head
        for i in range(right-left):
            right_node = right_node.next
        
        before, after = None, None
        for i in range(left-1):
            before = left_node
            left_node = left_node.next
            right_node = right_node.next
        after = right_node.next

        prev = after
        curr = left_node
        while curr and curr != after:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_

        if before:
            before.next = prev
            return head
        return prev
