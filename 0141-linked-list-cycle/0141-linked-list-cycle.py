# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slowp = head
        fastp = head

        while fastp and fastp.next:
            slowp = slowp.next
            fastp = fastp.next.next
            
            if slowp == fastp:
                return True
            
        return False
    

    def hasCycle_1(self, head: Optional[ListNode]) -> bool:
        nodeSet = set()

        temp = head

        while temp:
            if temp in nodeSet:
                return True
            
            nodeSet.add(temp)
            temp = temp.next

        return False
        