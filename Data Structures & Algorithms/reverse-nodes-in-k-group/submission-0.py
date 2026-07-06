# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tmp=head
        count=0
        l=[]
        while tmp is not None:
            count+=1
            tmp=tmp.next
        
        curr=head
        for i in range(count//k):
            prev=None
            for j in range(k):
                nn=curr.next
                curr.next=prev
                prev=curr
                curr=nn
            #print(nn.val)
            
            #prev1= prev
            l.append(prev)
            #if i==1:
            #    return prev
        #print(l[0].val)
        if count%k!=0:
            l.append(nn)
        nh=ListNode(l[0].val)
        tail=nh
        #return l
        for i in range(len(l)):
            for j in range(k):
                #print(l[i].val)
                tail.next=ListNode(l[i].val)
                tail=tail.next
                l[i]=l[i].next
                if l[i]==None:
                    break

        return nh.next