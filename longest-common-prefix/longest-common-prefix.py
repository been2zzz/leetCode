class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ''
        strs.sort(key=len,reverse=True)
        if len(strs) == 1:
            return strs[0]
        for i in range(len(strs[0])+1):
            answer = strs[0][:i]
            for j in range(1,len(strs)):
                if strs[j][:i] != answer:
                    return strs[0][:i-1]

        return answer
