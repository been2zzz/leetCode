class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {"(":")","{":"}","[":"]"}
        for i in range(len(s)):
            if s[i] in matches.keys():
                stack.append(matches[s[i]])
            else:
                if not stack:
                    return False
                elif stack[-1] == s[i]:
                    stack.pop(-1)
                else:
                    return False
        return len(stack) == 0