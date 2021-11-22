class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list =  s.split(" ")
        for i in range(len(list)-1,-1,-1):
            if list[i] != '':
                return len(list[i])
