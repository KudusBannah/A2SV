class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Moving to the middle
        fast_p = slow_p = head
        while fast_p:
            fast_p = fast_p.next.next
            slow_p = slow_p.next

        # reversing from the middle to the end
        prev, curr = None, slow_p
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        
        max_ = float('-inf')
        while prev:
            max_ = max(max_, (prev.val + head.val))
            prev = prev.next
            head = head.next
        return max_