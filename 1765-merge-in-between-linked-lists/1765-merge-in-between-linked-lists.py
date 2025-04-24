# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        def length(head):
            current=head
            count=0
            while(current):
                count+=1
                current=current.next
            return count   
        count=0
        current=list1
        prev=None
        while(current.next):
            if count==a: 
                last1=prev
            if count==b:
                last2=current.next
            prev=current
            current=current.next
            count+=1
        last1.next=list2 
        current2=list2
        while(current2.next):
            current2=current2.next
        current2.next=last2
        return list1