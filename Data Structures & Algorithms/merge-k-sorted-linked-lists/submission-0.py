# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists)==0:
            return None
        elif len(lists)==1:
            if len(lists[0])>0:
                return lists[0]
            else:
                return None

        for i in range(len(lists)-1):
            if i==0:
                l1=lists[0]
                l2=lists[1]
            else:
                l1=head
                l2=lists[i+1]

            if l1 is not None and l2 is not None:
                if l1.val>l2.val:
                    head=ListNode(l2.val)
                    tail=head
                    l2=l2.next
                else:
                    head=ListNode(l1.val)
                    tail=head
                    l1=l1.next
            elif l1 is None:
                head=l2
                return head
            else:
                head=l1
                return head              

            while l1 is not None or l2 is not None:
                #print(l1.val,l2.val)
                if l1 is not None:
                    if l2 is None:
                        tail.next=ListNode(l1.val)
                        tail=tail.next
                        l1=l1.next
                    else:
                        if l1.val>l2.val:
                            tail.next=ListNode(l2.val)
                            tail=tail.next
                            l2=l2.next
                        else:
                            tail.next=ListNode(l1.val)
                            tail=tail.next
                            l1=l1.next
                else:
                    tail.next=ListNode(l2.val)
                    tail=tail.next
                    l2=l2.next
            #print(tail.val)
        return head

            
