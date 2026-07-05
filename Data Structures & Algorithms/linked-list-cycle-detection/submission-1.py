# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is not None and head.next is not None:
            slow=head
            fast=head.next
        else:
            return False

        while fast is not None and slow is not None:
            if fast==slow:
                return True
            else:
                if fast.next is not None and slow is not None:
                    fast=fast.next.next
                    slow=slow.next
                else:
                    return False
                
        return False
