# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        temp = head 

        while temp and temp.next:
            nextNode = temp.next

            while nextNode and nextNode.val == temp.val:
                nextNode = nextNode.next
            
            temp.next = nextNode
            
            if nextNode:
                nextNode.prev = temp
            
            temp = temp.next
        
        return head