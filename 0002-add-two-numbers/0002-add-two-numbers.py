# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def spread_list(list):
            current = list
            answer = []
            while current:
                answer.append(current.val)
                current = current.next
            answer.reverse()
            return "".join(map(str, answer))
            
        l1_num = int(spread_list(l1))
        l2_num = int(spread_list(l2))
        answer: ListNode = None
        
        for i in str(l1_num+l2_num):
            node = ListNode(int(i))
            node.next = answer
            answer = node

        return answer