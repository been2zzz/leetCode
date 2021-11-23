# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = []
        # queue에 양쪽 노드 append
        queue.append((root.left, root.right))
        while queue:
            # 첫번째 노드 pop()
            node1, node2 = queue.pop(0)
            # 두 노드 다 없을 경우 건너뛰기
            if not node1 and not node2:
                continue
            # 한 노드만 있을 경우 notSymmetric
            elif not node1 or not node2:
                return False
            # val이 다를 경우 notSymmetric
            elif node1.val != node2.val:
                return False
            # 대칭이기에 서로 left, right로 비교
            queue.append((node1.left, node2.right))
            queue.append((node1.right, node2.left))
        return True