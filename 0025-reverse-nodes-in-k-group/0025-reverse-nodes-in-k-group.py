# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        prevLast = None

        while temp:
            kthNode = self.getKthNode(temp, k)

            if not kthNode:
                if prevLast:
                    prevLast.next = temp
                    break
                
            nextNode = kthNode.next

            kthNode.next = None

            self.reverseLinkedList(temp)

            if temp == head:
                head = kthNode
            else:                    
                prevLast.next = kthNode

            prevLast = temp
            temp = nextNode
            
        return head


    def getKthNode(self, temp, k):
        k -= 1

        while temp and k > 0:
            k -= 1
            temp = temp.next
        
        return temp
    
    def reverseLinkedList(self, head):
        
        temp = head
        prev = None

        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        return prev
        