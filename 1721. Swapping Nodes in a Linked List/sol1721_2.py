# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution_2:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        totalLen = self.getListLen(head)

        if totalLen == 1:
            return head
        elif totalLen == 2:
            firstVal = head.val
            secondVal = head.next.val
            head.val = secondVal
            head.next.val = firstVal
            return head
        elif totalLen == (k*2 -1):
            return head
        else:
            if (totalLen/2 < k) :
                k = totalLen - k + 1
            kHead = self.getKthPoint(head, k-1)
            kHeadVal = kHead.val
            rearKHead = self.getKthPoint(head, totalLen - k)
            rearKHeadVal = rearKHead.val
            kHead.val = rearKHeadVal
            rearKHead.val = kHeadVal
            return head
            
    def getListLen(self, input: Optional[ListNode]) -> int:
        count = 0
        while input != None:
            count+=1
            input = input.next
        return count
    
    def getKthPoint(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tempHead = head
        for i in range(k):
            tempHead = tempHead.next
        return tempHead
    