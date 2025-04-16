# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count=0
        temp=head
        while(temp is not None):
            count+=1
            temp=temp.next
        position_front=count-k
        if (count==k):
            head=head.next 
            return head
        i=1
        temp=head
        while(temp is not None):
            if(position_front==i):
                break
            temp=temp.next
            i+=1
        temp.next=temp.next.next
        return head