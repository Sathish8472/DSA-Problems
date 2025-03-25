# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            front = current.next
            current.next = prev
            prev = current
            current = front
        
        return prev

    def plusOne(self, head: ListNode) -> ListNode:

        head = self.reverseList(head)

        current = head
        carry = 1

        while current:
            current.val += carry
            if current.val < 10:
                carry = 0
                break
            
            current.val = 0
            if not current.next:
                current.next = ListNode(1)
                carry = 0
                break
            
            current = current.next
        
        return self.reverseList(head)
        