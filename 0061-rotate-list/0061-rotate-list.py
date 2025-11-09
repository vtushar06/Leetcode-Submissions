# Definition for singly-linked list.
 Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def length(head):
            count=1
            current=head
            while(current.next):
                count+=1
                current=current.next
            return count    
        if head is None:
            return None
        if head.next is None:
            return head  
              
        k = k % length(head)
        if k == 0:
            return head    
        end=head
        def reverse(head):
            prev=None
            current=head
            while(current):
                fornt=current.next
                current.next=prev
                prev=current
                current=fornt
            return prev
        newhead=reverse(head)
        for i in range(k):
            current=newhead
            newhead=newhead.next
            end.next=current
            current.next=None
            end=current
        return reverse(newhead)           
        
