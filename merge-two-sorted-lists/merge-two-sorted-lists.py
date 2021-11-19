# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        dummy = head
        # l1과 l2 모두 있을 때만 반복
        while(l1 and l2):
            if l1.val < l2.val: 
                # dummy.next에 l1 
                dummy.next = l1
                # 처리한 노드 제외 l1 
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        # 남은 노드 dummy.next 
        dummy.next = l1 or l2
        return head.next
                