class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        i = 0
        while True:
            if len(s) == i:
                break
            if (s[i] == 'I' or s[i] == 'X' or s[i] == 'C') and len(s) != i+1 :
                if d[s[i+1]] > d[s[i]]:
                    answer += d[s[i+1]] - d[s[i]]
                    i += 2
                else:
                    answer += d[s[i]]
                    i += 1                    
            else:
                answer += d[s[i]]
                i += 1
        return answer