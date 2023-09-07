# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        indices_dict = {}
        curr, i = head, 0
        while curr:
            indices_dict[curr] = i
            curr = curr.next
            i += 1
        
        stack = []
        output = [0] * i
        curr = head
        while curr:
            while stack and curr.val > stack[-1].val:
                popped = stack.pop()
                idx = indices_dict[popped]
                output[idx] = curr.val

            stack.append(curr)
            curr = curr.next
        return output
