# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count=0
        while curr:
            count+=1
            curr = curr.next

        removeIn = count - n
        if removeIn == 0:
            return head.next

        curr_again = head
        count_again = 0
        while curr_again:
            if count_again == removeIn-1:
                curr_again.next =  curr_again.next.next
                break
            curr_again = curr_again.next
            count_again+=1
        return head