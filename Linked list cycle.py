# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        met = set()
        while current:
            if current in met:
                return True
            met.add(current)
            current = current.next
        return False