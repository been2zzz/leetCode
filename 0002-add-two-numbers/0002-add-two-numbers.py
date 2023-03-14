# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 연결리스트 -> 역순 연결리스트로 만드는 함수
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
            
        return prev
    
    # 연결리스트 -> 배열로 만드는 함수
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list
    
    # 문자열 -> 역순 연결리스트 변환 함수
    def reverseLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        
        for i in result:
            node = ListNode(i)
            node.next = prev
            prev = node
        
        return node
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        result = int(''.join(map(str,a))) + int(''.join(map(str,b)))
        return self.reverseLinkedList(str(result))
        
    
        