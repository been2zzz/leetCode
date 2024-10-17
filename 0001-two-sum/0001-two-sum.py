class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for idx, num in enumerate(nums):
            dic[num] = idx
        for idx, num in enumerate(nums):
            need = target - num
            if need in dic and dic[need] != idx:
                return sorted([dic[need], idx])
        return []
        