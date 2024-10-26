# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        even_head = even 

        # 홀수, 짝수 노드를 번갈아 연결
        while even and even.next:   
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        # 홀수 리스트 끝에 짝수 리스트 연결
        odd.next = even_head

        return head
