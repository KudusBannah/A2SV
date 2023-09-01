# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_node = odd_tail = ListNode()
        even_node = even_tail = ListNode()
        i = 0
        while head:
            if i%2 == 0:
                odd_tail.next = head
                odd_tail = head
            else:
                even_tail.next = head
                even_tail = head
            i += 1
            head = head.next

        even_tail.next = None
        odd_tail.next = even_node.next
        return odd_node.next
