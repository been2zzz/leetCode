import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        manipulateStr = s.replace(" ","")
        manipulateStr = re.sub(r'[^A-Za-z0-9\s]', '', manipulateStr)
        manipulateStr = manipulateStr.lower()
        first = manipulateStr[:len(manipulateStr)//2]
        if len(manipulateStr) % 2 == 1:
            second = manipulateStr[len(manipulateStr)//2+1:]
        else:
            second = manipulateStr[len(manipulateStr)//2:]
        print(first, second)

        return first == second[::-1]