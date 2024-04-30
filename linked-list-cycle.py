(* https://leetcode.com/problems/linked-list-cycle/ *)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        flag = 'f'
        while head:
            if head.val == 'f': return True
            else: head.val = 'f'
            head = head.next
        return False
        # read = []
        # while head:
        #     if head in read: return True
        #     else: read.append(head)
        #     head = head.next
        # return False
