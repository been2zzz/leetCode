class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
		
        def backtracking(start, curr):
            result.append(curr[:])
            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtracking(i+1, curr)
                curr.pop()
                
        backtracking(start = 0, curr = [])
        return result