# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findAncestors(root, target):
            if root == target:
                return [target]
            
            if root.val > target.val:
                return [root] + findAncestors(root.left, target)
            return [root] + findAncestors(root.right, target)

        p_ancestors = findAncestors(root, p)
        q_ancestors = set(findAncestors(root, q))
        
        for i in range(len(p_ancestors)-1, -1, -1):
            if p_ancestors[i] in q_ancestors:
                return p_ancestors[i]