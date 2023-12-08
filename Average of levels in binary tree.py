# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        average_sum = []
        while queue:
            curr_sum = 0
            len_ = len(queue)
            for i in range(len_):
                curr = queue[0]
                if queue[0].left: queue.append(queue[0].left)
                if queue[0].right: queue.append(queue[0].right)
                queue.popleft()
                curr_sum += curr.val
            average_sum.append(curr_sum/len_)
        return average_sum
