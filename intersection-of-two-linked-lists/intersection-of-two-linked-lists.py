# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        def getSize(head):
            size = 0
            while head:
                head = head.next
                size += 1
            return size
        sizeA = getSize(headA)
        sizeB = getSize(headB)
        # while문 시작점을 맞추기 위해 큰 ListNode를 headA로 바꿔줌
        if sizeA < sizeB:
            sizeA, sizeB = sizeB, sizeA
            headA, headB = headB, headA
        remain = sizeA - sizeB
        while remain:
            headA = headA.next
            remain -= 1
        
        while (headA and headB):
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None