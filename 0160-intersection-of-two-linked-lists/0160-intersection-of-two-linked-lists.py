# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def length(head):
            current=head
            count=0
            while(current):
                current=current.next
                count+=1
            return count
        lenA=length(headA)
        lenB=length(headB)
        while(lenA>lenB):
            lenA-=1
            headA=headA.next
        while(lenB>lenA):
            lenB-=1
            headB=headB.next
        currA=headA
        currB=headB
        while(currA!=currB):
            currA=currA.next
            currB=currB.next
        return currA                        


