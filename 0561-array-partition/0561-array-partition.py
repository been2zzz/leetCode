class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2]) # 슬라이싱 구문 사용. 한 칸씩 건너뜀