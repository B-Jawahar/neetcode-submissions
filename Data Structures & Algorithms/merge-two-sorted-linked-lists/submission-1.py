# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            if list2 is None:
                return None
            else:
                return list2
        if list2 is None:
                return list1
        if list1.val<list2.val:
            head=ListNode(list1.val)
            tail=head
            curr1=list1.next
            curr2=list2
        else:
            head=ListNode(list2.val)
            tail=head
            curr1=list1
            curr2=list2.next

        while curr1 is not None or curr2 is not None:
            if curr1==None:
                print("curr1 none",curr2.val)
                tail.next=ListNode(curr2.val)
                tail=tail.next
                curr2=curr2.next
            elif curr2==None:
                print("curr2 none",curr1.val)
                tail.next=ListNode(curr1.val)
                tail=tail.next
                curr1=curr1.next
            elif curr1.val<=curr2.val:
                print("curr1 small than curr2",curr1.val)
                tail.next=ListNode(curr1.val)
                tail=tail.next
                curr1=curr1.next
            else:
                print("curr2 small than curr1",curr2.val)
                tail.next=ListNode(curr2.val)
                tail=tail.next
                curr2=curr2.next
        return head