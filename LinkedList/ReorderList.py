# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self,head:Optional[ListNode]) -> None:
        prev, curr = None, head
        while curr:
            nxt = curr.next

            curr.next = prev            
            prev = curr
            curr = nxt
        return prev


    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        # Split into 2 parts
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

        pre_second = slow.next # start the 2nd half
        slow.next = None # cut first half
        second = self.reverseList(pre_second)

        first = head
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
            

