# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first=l1
        second=l2
        carry=0
        dummy=ListNode(0)
        current=dummy
        while(first or second or carry):
            val1=first.val if first else 0
            val2=second.val if second else 0
            total=val1+val2+carry
            carry=total//10
            digit=total%10
            new_node=ListNode(digit)
            current.next=new_node
            current=new_node

            if first:
                first=first.next
            if second:
                second=second.next
        return dummy.next            


