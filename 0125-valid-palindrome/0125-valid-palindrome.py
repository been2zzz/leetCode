import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        manipulateStr = s.replace(" ","")
        manipulateStr = re.sub(r'[^A-Za-z0-9\s]', '', manipulateStr)
        manipulateStr = manipulateStr.lower()
        return manipulateStr == manipulateStr[::-1]
