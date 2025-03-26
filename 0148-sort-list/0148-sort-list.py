# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # USing Merge sort
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        middle = self.findMiddle(head)

        right = middle.next
        middle.next = None
        left = head

        left = self.sortList(left)
        right = self.sortList(right)

        return self.mergeTwoSortedLinkedList(left, right)

    def mergeTwoSortedLinkedList(self, list1, list2):
        dummyNode = ListNode(-1)
        temp = dummyNode

        while list1 and list1:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            
            temp = temp.next
        
        if list1:
            temp.next = list1
        else:
            temp.next = list2
        
        return dummyNode.next


    def findMiddle(self, head):
        if not head or not head.next:
            return head
        
        slow = head
        fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow


    # Brute
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        temp = head

        while temp:
            arr.append(temp.val)
            temp = temp.next
        
        arr.sort()

        temp = head
        i = 0
        while temp:
            temp.val = arr[i]
            temp = temp.next
            i += 1
        
        return head
            
        