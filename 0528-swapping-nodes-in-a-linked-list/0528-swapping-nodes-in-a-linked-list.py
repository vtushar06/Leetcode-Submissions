# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current=head
        count=0
        while(current):
            count+=1
            current=current.next
        front=head
        for _ in range(1,k) :
            front=front.next 
        end=head
        for _ in range(1,count-k+1):
            end=end.next
        front.val,end.val=end.val,front.val
        return head          
    


        