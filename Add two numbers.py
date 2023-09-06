class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        i = 0
        while l1 or l2:
            if l1 and l2:
                num += (l1.val*(10**i)) + (l2.val*(10**i))
                l1 = l1.next
                l2 = l2.next
            elif l1:
                num += (l1.val*(10**i))
                l1 = l1.next
            else:
                num += (l2.val*(10**i))
                l2 = l2.next
            i += 1
        dummy = curr_node = ListNode()
        for dig in str(num):
            curr_node.next = ListNode(int(dig))
            curr_node = curr_node.next
        
        prev = None
        curr = dummy.next
        while curr and curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        return prev