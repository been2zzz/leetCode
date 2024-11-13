# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total = 0

        def sumNode(node):
            if not node:
                return 0

            # 오른쪽 -> 루트 -> 왼쪽 순으로 순회
            sumNode(node.right)

            if low <= node.val <= high:
                self.total += node.val

            sumNode(node.left)

        sumNode(root)
        return self.total     