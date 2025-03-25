# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addHelper(self, temp: ListNode) -> int:
        if temp is None:
            return 1
        
        carry = self.addHelper(temp.next)
        temp.val += carry

        if temp.val < 10:
            return 0
        
        temp.val = 0
        return 1

    def plusOne(self, head: ListNode) -> ListNode:
        carry = self.addHelper(head)

        if carry == 1:
            newNode = ListNode(1)
            newNode.next = head
            head = newNode
        
        return head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            front = current.next
            current.next = prev
            prev = current
            current = front
        
        return prev


    # Brute force
    def plusOne_1(self, head: ListNode) -> ListNode:

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
        