class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        temp = ''
        
        for target in s:
            if target in temp:
                # Remove characters from the beginning of `temp` up to and including the first occurrence of `target`
                temp = temp[temp.index(target) + 1:]
            temp += target
            max_length = max(max_length, len(temp))
        
        return max_length