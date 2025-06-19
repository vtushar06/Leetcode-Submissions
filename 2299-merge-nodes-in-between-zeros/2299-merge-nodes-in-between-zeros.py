# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head.next
        dummy=ListNode()
        currentdummy=dummy
        ans=0
        while(current):
            if(current.val==0):
                node=ListNode(ans)
                currentdummy.next=node
                currentdummy=node
                
                ans=0
            else:
                ans+=current.val
            current=current.next
        
        return dummy.next
        