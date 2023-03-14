# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            # Store the two nodes to be swapped
            a = prev.next
            b = prev.next.next

            # Perform the swap
            prev.next = b
            a.next = b.next
            b.next = a

            # Update the pointers
            prev = a

        return dummy.next
        