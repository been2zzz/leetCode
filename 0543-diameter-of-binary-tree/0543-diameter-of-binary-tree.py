# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0  # 최대 지름 저장용
        
        def depth(node):
            if not node:
                return 0  # 노드가 없는 경우 깊이 0
            
            # 왼쪽과 오른쪽의 깊이를 재귀적으로 계산
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            print(left_depth, right_depth)
            # 현재 노드에서 지름 업데이트 (left + right 경로)
            self.diameter = max(self.diameter, left_depth + right_depth)
            
            # 현재 노드의 깊이를 반환
            return max(left_depth, right_depth) + 1
        
        depth(root)
        return self.diameter
