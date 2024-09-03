class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        temp = ''
        
        for target in s:
            if target in temp:
                temp = temp[temp.index(target) + 1:]
            temp += target
            max_length = max(max_length, len(temp))
        
        return max_length