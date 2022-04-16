# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        totalLen = self.getListLen(head)
        if (k > totalLen/2):
            k = totalLen + 1 - k
            print("111")
        if (k == 1 and totalLen == k):
            return head
        
        kPoint = self.moveKth(head, k)
        endkPoint = self.moveKth(head, totalLen-k+1)
        
        
        if (totalLen == 2):
            endkpostPoint = self.moveKth(head, totalLen-k+2)
            
            kPoint.next = endkpostPoint
            endkPoint.next = kPoint
            head = endkPoint
            return head
        if (totalLen % 2 == 0 and totalLen / 2 == k) :
            kprevPoint = self.moveKth(head, k-1)
            endkpostPoint = self.moveKth(head, totalLen-k+2)
            
            kPoint.next = endkpostPoint
            endkPoint.next = kPoint
            kprevPoint.next = endkPoint
            return head
        
        if (k == 1):
            endkprevPoint = self.moveKth(head, totalLen-k)
            endkpostPoint = self.moveKth(head, totalLen-k+2)
            kpostPoint = self.moveKth(head, k+1)
            
            kPoint.next = endkpostPoint
            endkprevPoint.next = kPoint
            endkPoint.next = kpostPoint
            head = endkPoint
        else:
            kprevPoint = self.moveKth(head, k-1)
            kpostPoint = self.moveKth(head, k+1)
            endkprevPoint = self.moveKth(head, totalLen-k)
            endkpostPoint = self.moveKth(head, totalLen-k+2)
            
            kPoint.next = endkpostPoint
            kprevPoint.next = endkPoint
            endkPoint.next = kpostPoint
            endkprevPoint.next = kPoint

        return head
            
        print('kth value is ' + str(kPoint.val))
        print('endkth value is ' + str(endkPoint.val))
        print('List total Length ' + str(totalLen))
        
    def getListLen(self, input: Optional[ListNode]) -> int:
        count = 0
        while input != None:
            count+=1
            input = input.next
        return count
    
    def moveKth(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        for i in range(k-1):
            head = head.next
        return head
    