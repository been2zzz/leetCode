class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_string = ''.join(filter(str.isalnum, s))
        for i in range(len(new_string)//2):
            if new_string[i] != new_string[-i-1]:
                return False
        return True