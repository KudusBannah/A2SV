# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def sort(list1, list2):
            dummy = curr = ListNode()
            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next
            
            if list1:
                curr.next = list1
            else:
                curr.next = list2
            return dummy.next
        
        if len(lists) == 0: return None

        if len(lists) == 1: return lists[0]
        
        ans = sort(lists[0], lists[1])
        for i in range(2, len(lists)):
            ans = sort(ans, lists[i])
        return ans
            
        
        