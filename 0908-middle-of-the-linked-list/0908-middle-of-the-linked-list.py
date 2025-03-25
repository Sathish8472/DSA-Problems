# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode1(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def middleNode(self, head):
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    # Brute
    def middleNode_1(self, head):
        counter = 0

        temp = head

        while temp:
            counter += 1
            temp = temp.next
        
        temp = head
        middle_node = counter // 2 + 1

        while temp:
            middle_node -= 1
            if middle_node == 0:
                break
            
            temp = temp.next
        
        return temp
