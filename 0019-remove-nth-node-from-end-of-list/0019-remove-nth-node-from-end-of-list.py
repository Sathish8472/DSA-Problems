# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fastp = head
        slowp = head

        for _ in range(n):
            fastp = fastp.next
        
        if not fastp:
            return head.next
        
        while fastp.next:
            fastp = fastp.next
            slowp = slowp.next
        
        slowp.next = slowp.next.next

        return head
    


    def removeNthFromEnd_1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head:
            return None
        
        count = 0
        temp = head

        while temp:
            count += 1
            temp = temp.next

        if count == n:
            return head.next

        res = count - n
        temp = head

        while res > 1:
            res -= 1
            temp = temp.next
        
        temp.next = temp.next.next
        return head