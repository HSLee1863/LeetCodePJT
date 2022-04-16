# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution_3:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        leftNode = head
        for _ in range(k-1):
            leftNode = leftNode.next
            
        tempLeftStartNode = leftNode
        rightNode = head
        while tempLeftStartNode.next != None:
            tempLeftStartNode = tempLeftStartNode.next
            rightNode = rightNode.next
            
        leftNode.val, rightNode.val = rightNode.val, leftNode.val
        
        return head