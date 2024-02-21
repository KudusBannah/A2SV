# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dp(curr, flag):
            if not curr:
                return 0

            if (curr, flag) not in memo:

                if flag:
                    memo[(curr, flag)] = dp(curr.left, False) + dp(curr.right, False)
                else:
                    a = dp(curr.left, False) + dp(curr.right, False)
                    b = dp(curr.right, True) + dp(curr.left, True) + curr.val
                    memo[(curr, flag)] = max(a, b)

            return memo[(curr, flag)]
        
        return dp(root, False)