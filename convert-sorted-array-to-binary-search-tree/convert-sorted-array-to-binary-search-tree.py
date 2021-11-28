# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # nums 배열 비었을 경우
        if len(nums) == 0:
            return None
        # 하나일 경우
        elif len(nums) == 1:
            return TreeNode(nums[0])
        else:
            # 정렬된 배열이기에 2 나눈 몫 index가 최상단 노드
            mid = len(nums) // 2
            node = TreeNode(nums[mid])
            # 작은 값 left 노드, 큰 값 right 노드
            node.left = self.sortedArrayToBST(nums[:mid])
            node.right = self.sortedArrayToBST(nums[mid+1:])
        return node
            