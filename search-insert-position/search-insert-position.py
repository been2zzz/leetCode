class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        start = 0
        end = len(nums) - 1
        result = 0 
        while(start <= end):
            mid = (start + end) // 2
            
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        print(start,end)
        return start