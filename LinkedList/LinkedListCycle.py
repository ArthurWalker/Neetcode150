# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # visited_node = []
        # curr = head
        # while curr:
        #     if curr in visited_node:
        #         return True
        #     visited_node.append(curr)
        #     curr = curr.next
        # return False

        slow,fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
