# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Finding the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reversing the list from the middle section
        prev = None
        curr = slow
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        
        # Checking if they are palindromes
        head1, head2 = head, prev
        while head1 and head2:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        return True