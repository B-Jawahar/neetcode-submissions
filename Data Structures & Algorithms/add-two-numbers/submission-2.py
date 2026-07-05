# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        addval=(l1.val+l2.val)
        c=0
        if addval>9:
            addval-=10
            c=1
        result=ListNode(addval)
        tail=result

        l1=l1.next
        l2=l2.next

        while l1 is not None or l2 is not None:
            if l1 is not None and l2 is not None:
                addval=(l1.val+l2.val)
                if c==1:
                    addval+=1
                if addval>9:
                    addval-=10
                    c=1
                else:
                    c=0
                print(addval)
                tail.next=ListNode(addval)
                tail=tail.next
                l1=l1.next
                l2=l2.next
            elif l1 is not None:
                print(l1.val)
                if c==1:
                    addval=l1.val+1
                else:
                    addval=l1.val
                if addval>9:
                    addval-=10
                    c=1
                else:
                    c=0
                print("l1",addval)
                tail.next=ListNode(addval)
                tail=tail.next
                l1=l1.next
            else:
                if c==1:
                    addval=l2.val+1
                else:
                    addval=l2.val
                if addval>9:
                    addval-=10
                    c=1
                else:
                    c=0
                print("l2",addval)
                tail.next=ListNode(addval)
                tail=tail.next
                l2=l2.next
        if c==1:
            tail.next=ListNode(1)
            tail=tail.next

        return result