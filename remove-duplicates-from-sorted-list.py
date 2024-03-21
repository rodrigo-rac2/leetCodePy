# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head == None:
#             return None
#         result = ListNode()
#         result.val = head.val
#         tail = result
#         while head.next != None:
#             if not self.listNodeContains(head.val, result):
#                 tempNode = ListNode()
#                 tempNode.val = head.val
#                 tail.next = tempNode
#                 tail = tail.next
#             head = head.next
#         if not self.listNodeContains(head.val, result):
#             tempNode = ListNode()
#             tempNode.val = head.val
#             tail.next = tempNode
#             tail = tail.next
#         return result
    
#     def listNodeContains(self, val, head) -> bool:
#         if head.val == val: return True
#         while head.next != None:
#             if head.val == val:
#                 return True
#             head = head.next
#         if head.val == val: return True
#         return False

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        result = ListNode()
        result.val = head.val
        tail = result
        added = set()
        added.add(head.val)
        while head.next != None:
            if not head.val in added:
                tempNode = ListNode()
                tempNode.val = head.val
                tail.next = tempNode
                tail = tail.next
                added.add(head.val)
            head = head.next
        # check the last
        if not head.val in added:
            tempNode = ListNode()
            tempNode.val = head.val
            tail.next = tempNode
            tail = tail.next
        return result
