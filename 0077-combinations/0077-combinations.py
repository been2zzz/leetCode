class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]  
        result = []  
        
        def backtracking(start, curr):
            if len(curr) == k:
                result.append(curr[:])
                return

            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtracking(i + 1, curr)  
                curr.pop()
        
        backtracking(0, [])  
        return result
