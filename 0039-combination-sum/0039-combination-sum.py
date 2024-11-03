class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []  
        
        def backtracking(start, curr, current_sum):
            if current_sum > target:
                return

            if current_sum == target:
                result.append(curr[:])
                return

            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                backtracking(i, curr, current_sum + candidates[i])  
                curr.pop()
        
        backtracking(0, [], 0)  
        return result