# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        N, curr = 0, head
        while curr:
            N += 1
            curr = curr.next
        loops = N // k

        dummy = curr_dummy = ListNode()
        l_node = r_node = head
        
        for i in range(loops):
            for i in range(k-1):
                r_node = r_node.next
            after = r_node.next

            prev, curr = after, l_node
            while curr and curr != after:
                next_ = curr.next
                curr.next = prev
                prev = curr
                curr = next_
            curr_dummy.next = prev
            curr_dummy = l_node
            l_node = r_node = after
        return dummy.next
        