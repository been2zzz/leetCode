class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = []
        for i in s:
            if i.isalnum():
                str.append(i.lower())
        reverseStr = str.copy()
        reverseStr.reverse()
        for i in range(len(str)):
            if str[i] != reverseStr[i]:
                return False
        return True