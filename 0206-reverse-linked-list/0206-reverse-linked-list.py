# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        temp = head
        prev = None

        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        return prev





    # Stack Approach
    # Time: O(N), Space: O(N)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        temp = head

        while temp:
            stack.append(temp.val)
            temp = temp.next

        temp = head
        while temp:
            temp.val = stack.pop()
            temp = temp.next
        
        return head
        