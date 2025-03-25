# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # Optimal Solution
    # Time: O(N), Space: O(1)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half_head = self.reverse(slow)

        first_half, second_half = head, second_half_head

        while second_half:
            if first_half.val != second_half.val:
                return False
            
            first_half = first_half.next
            second_half = second_half.next
        
        self.reverse(second_half_head)

        return True

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            front = current.next
            current.next = prev
            prev = current
            current = front
        
        return prev

    # Brute
    # Time: O(N), SpacE: O(N)

    def isPalindrome_1(self, head: Optional[ListNode]) -> bool:
        stack = []
        temp = head

        while temp:
            stack.append(temp.val)
            temp = temp.next

        temp = head

        while temp:
            if temp.val != stack.pop():
                return False
            temp = temp.next
        
        return True

        
        