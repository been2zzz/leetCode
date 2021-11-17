class Solution:
    def isPalindrome(self, x: int) -> bool:
        list = []
        for i in str(x):
            list.append(str(i))
        for i in range(len(list)//2):
            print(list[i],list[-1-i])
            if list[i] != list[-1-i]:
                return False
        return True