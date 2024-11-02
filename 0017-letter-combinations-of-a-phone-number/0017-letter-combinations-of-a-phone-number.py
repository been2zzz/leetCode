class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return
            for char in dic[digits[index]]:
                dfs(index + 1, path + char)

        if not digits:
            return []
        dic = {"2":"abc", "3":"def","4":"ghi", "5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result = []
        dfs(0, "")
        return result