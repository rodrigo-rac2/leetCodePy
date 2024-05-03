# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head:
            if head.val == val:
                head = head.next
            else:
                break
        tail = head
        while tail:
            if tail.next and tail.next.val == val:
                if tail.next.next:
                    tail.next = tail.next.next
                else:
                    tail.next = None
            else: tail = tail.next
        return head
        # new_head = None
        # while head:
        #     if head.val != val: 
        #         if not new_head:
        #             new_head = new_runner = ListNode(head.val)
        #         else: 
        #             new_runner.next = ListNode()
        #             new_runner = new_runner.next
        #             new_runner.val = head.val
        #     head = head.next
        # return new_head
