# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Approach: two pointers/fast and slow and Left ko dummy mein dedo
# TC:O(n)
# SC: O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # next pointr of dummy is set to head. list= 1 2 3 4 5 n = 2 
        dummy = ListNode(0,head)
        left = dummy    #left = DN 
        right = head    #right = 1

        # right ko n se move karo
        while n > 0 and right:  #n = 2,1,0
            right = right.next  #right = 2,3 
            n -=1    #agar n = 0 hogaya matlab shift karliya jitna karna tha

        # keep shifting both the ptr till right reaches end
        while right:
            left = left.next    #1,2,3
            right = right.next  #4,5,null

        # delete eg: 3->4->5 left at 3 
        left.next = left.next.next
        
        return dummy.next
        