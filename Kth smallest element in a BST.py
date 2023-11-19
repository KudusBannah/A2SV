# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # perform depth First Search
        arr = []
        def search(node):
            nonlocal arr
            if not node:
                return
            
            search(node.left)
            search(node.right)
            arr.append(node.val)
        
        search(root)
        heapify(arr)
        for i in range(k-1):
            heappop(arr)
        return arr[0]
        