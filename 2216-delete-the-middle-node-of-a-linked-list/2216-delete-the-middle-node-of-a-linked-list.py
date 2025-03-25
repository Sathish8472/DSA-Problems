# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return None

        temp = head
        n = 0

        while temp:
            n += 1
            temp = temp.next
        
        middleIndex = n // 2

        temp = head

        for _ in range(1, middleIndex):
            temp = temp.next
        
        if temp.next:
            middle = temp.next
            temp.next = temp.next.next
        
        return head