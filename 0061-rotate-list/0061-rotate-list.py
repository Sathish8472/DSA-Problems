# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        
        old_tail.next = head

        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next

        new_tail.next = None

        return new_head
    

    # Brute 
    def rotateRight_1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        temp = head
        length = 1
        while temp.next:
            length += 1
            temp = temp.next
        
        temp.next = head
        k = k % length

        end = length - k

        while end > 0:
            temp = temp.next
            end -= 1

        
        return head

        