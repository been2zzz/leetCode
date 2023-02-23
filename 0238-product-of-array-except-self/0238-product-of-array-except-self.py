class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1 # 곱한 값
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        
        p = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
            
        return out
        # Time limit
#         results = []
#         def multiply(arr):
#             if 0 in arr:
#                 return 0
#             return reduce(lambda x, y: x * y, arr)
#         for i in range(len(nums)):
#             if i == 0:
#                 results.append(multiply(nums[1:]))
#             elif i == len(nums)-1:
#                 results.append(multiply(nums[:-1]))
#             else:
#                 results.append(multiply(nums[:i]+nums[i+1:len(nums)]))

        
#         return results
        

