# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow=head
        fast=head
        for i in range(n):
            if(fast.next==None):
                if(i==n-1):
                    head=head.next
                return head
            fast=fast.next
        
        while(fast.next):
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return head
        