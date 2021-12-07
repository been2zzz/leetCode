class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1, idx2 = 0, len(numbers) -1
        while idx1 < idx2:
            if numbers[idx1] + numbers[idx2] == target:
                return [idx1 + 1, idx2 + 1]
            elif numbers[idx1] + numbers[idx2] < target:
                idx1 += 1
            else:
                idx2 -= 1
                