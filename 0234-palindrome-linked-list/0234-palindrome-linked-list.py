# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            if head is None:
                return head
            prev=None
            current=head
            while(current):
                front=current.next
                current.next=prev
                prev=current
                current=front   
            return prev    
        slow=fast=head
        while(fast.next and fast.next.next):
            slow=slow.next
            fast=fast.next.next
        first=head
        second=reverse(slow.next)
        while(second):
            if second.val !=first.val:
                return False
            first=first.next
            second=second.next 
        return True      

    

        