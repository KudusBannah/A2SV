# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(curr, start, end):
            if not curr:
                return True

            if curr.val <= start or curr.val >= end:
                return False

            a = valid(curr.left, min(start, curr.val), min(end, curr.val))
            b = valid(curr.right, max(start, curr.val), max(end, curr.val))
            return a and b

        return valid(root, float("-inf"), float('inf'))