# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def insertEnd(head, newNode):
            if head is None:
                head = newNode
            else:
                current = head
                while current.next is not None:
                    current = current.next
                current.next = newNode
            return head
        
        head = None  # This will be the merged list head
        currentFirst = list1
        currentSecond = list2

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        while currentFirst and currentSecond:
            if currentFirst.val < currentSecond.val:
                currentfirstnext = currentFirst.next
                currentFirst.next = None
                head = insertEnd(head, currentFirst)
                currentFirst = currentfirstnext
            else:
                currentsecondnext = currentSecond.next
                currentSecond.next = None
                head = insertEnd(head, currentSecond)
                currentSecond = currentsecondnext

        while currentFirst:
            currentfirstnext = currentFirst.next
            currentFirst.next = None
            head = insertEnd(head, currentFirst)
            currentFirst = currentfirstnext

        while currentSecond:
            currentsecondnext = currentSecond.next
            currentSecond.next = None
            head = insertEnd(head, currentSecond)
            currentSecond = currentsecondnext

        return head