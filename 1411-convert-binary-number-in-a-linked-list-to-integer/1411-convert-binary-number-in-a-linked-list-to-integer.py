# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        current=head
        count=0
        while(current):
            current=current.next
            count+=1
        pow=count-1
        ans=0
        node=head
        while(pow>=0):
            ans=ans+node.val*(2**pow)
            node=node.next
            pow-=1
        return ans    


