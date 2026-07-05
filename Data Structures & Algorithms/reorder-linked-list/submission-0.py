# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head.next

        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        
        sh=slow.next
        prev=slow.next=None

        while sh is not None:
            nn=sh.next
            sh.next=prev
            prev=sh
            sh=nn

        fh,sh=head,prev

        while sh:
            tmp1=fh.next
            tmp2=sh.next
            fh.next=sh
            sh.next=tmp1
            sh=tmp2
            fh=tmp1





        