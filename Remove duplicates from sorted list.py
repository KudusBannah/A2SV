# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        my_dict = defaultdict(int)
        curr = head
        prev = None
        while curr:
            next_ = curr.next
            if my_dict[curr.val]:
                prev.next = next_
                curr.next = None
            else:
                my_dict[curr.val] += 1
            if curr.next: prev = curr
            curr = next_
        return head