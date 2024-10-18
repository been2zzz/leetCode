# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        max_depth = 0
        if root is None:
            return max_depth
        queue.append((root, 1))
        while queue:
            cur_node, cur_depth = queue.popleft()
            max_depth = max(cur_depth, max_depth)
            if cur_node.left:
                queue.append((cur_node.left, cur_depth + 1))
                
            if cur_node.right:
                queue.append((cur_node.right, cur_depth + 1))
        return max_depth