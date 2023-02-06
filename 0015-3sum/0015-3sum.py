class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        nums.sort()
        for i in range(len(nums)):
            left, right = i+1, len(nums) -1
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    answer.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -=1
        return list(answer)