# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = current = ListNode(0)
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
            
        return head.next
        
        # 재귀 사용
        # if (not list1) or (list2 and list1.val > list2.val):
        #     list1, list2 = list2, list1
        # if list1:
        #     list1.next = self.mergeTwoLists(list1.next, list2)
        # return list1