# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return None

        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next
        
        return head
        
    

    def deleteMiddle_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return None

        counter = 0
        temp = head

        while temp:
            counter += 1
            temp = temp.next
        
        middle_index = counter // 2
        temp = head

        for _ in range(1, middle_index):
            temp = temp.next
        
        if temp.next:
            temp.next = temp.next.next
        
        return head
        