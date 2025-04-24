# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev=None
            current=head
            while(current):
                front=current.next
                current.next=prev
                prev=current
                current=front
            return prev
        head=reverse(head)    
        current=head
        maxi=current.val
        while(current and current.next):
            if current.next.val < maxi:   
                current.next=current.next.next
            else:
                current=current.next
                maxi=current.val
        return reverse(head)                 
        