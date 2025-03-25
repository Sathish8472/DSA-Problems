# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # Optimal - Two Pointers
    # time: O(M + n), Space: O(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        pA, pB = headA, headB

        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        
        return pA

    
    # Better
    # time: O(M + N), Space: O(M)
    def getIntersectionNode_2(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()

        while headA:
            visited.add(headA)
            headA = headA.next
        
        while headB:
            if headB in visited:
                return headB
            headB = headB.next
        
        return None

    # Brute
    # time: O(M * N), SpacE: O(1)
    def getIntersectionNode_1(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tempA = headA
        while tempA:
            tempB = headB
            
            while tempB:
                if tempA == tempB:
                    return tempA
                
                tempB = tempB.next
            tempA = tempA.next
        
        return None
        