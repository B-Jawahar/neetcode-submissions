# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        mov=head

        count=0

        while mov is not None:
            mov=mov.next
            count+=1

        if n==count:
            return head.next

        n=count-n
        mov=head
        for i in range(n):
            prevmov=mov
            mov=mov.next
        prevmov.next=mov.next
        return head

