# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        evenHead = head.next

        while even and even.next:

            odd.next = odd.next.next
            even.next = even.next.next
            
            odd = odd.next
            even = even.next

        odd.next = evenHead

        return head


    # Brute force
    # Time: O(N), Space: O(N)
    def oddEvenList_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        arr = []            # Additional Space
        temp = head

        while temp and temp.next:
            arr.append(temp.val)
            temp = temp.next.next

        if temp:
            arr.append(temp.val)
        
        temp = head.next
        
        while temp and temp.next:
            arr.append(temp.val)
            temp = temp.next.next
        
        if temp:
            arr.append(temp.val)

        i = 0
        temp = head
        
        while temp:
            temp.val = arr[i]
            i += 1
            temp = temp.next
        
        return head
        