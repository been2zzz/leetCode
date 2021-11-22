class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''
        for i in digits:
            string += str(i)
        string = str(int(string) + 1)
        answer = []
        for i in string:
            answer.append(int(i))
        return answer