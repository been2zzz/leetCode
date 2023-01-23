class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        no = list(set(nums))
        return not len(no) == len(nums)