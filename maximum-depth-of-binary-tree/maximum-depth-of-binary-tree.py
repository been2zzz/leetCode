# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = []
        depth = 0
        # 처음 depth 1
        q.append((1,root))
        while q:
            # 현재 depth, node
            cur_depth, root = q.pop(0)
            
            if root is not None:
                depth = max(depth, cur_depth)
                # 현재 depth + 1
                q.append((cur_depth+1,root.left))
                q.append((cur_depth+1,root.right))
        
        return depth