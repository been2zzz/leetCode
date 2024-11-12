# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0

        def reverse_inorder(node):
            if not node:
                return

            # 오른쪽 -> 루트 -> 왼쪽 순으로 순회
            reverse_inorder(node.right)

            # 현재 노드 값을 누적 합으로 변경
            self.total += node.val
            node.val = self.total

            reverse_inorder(node.left)

        reverse_inorder(root)
        return root        