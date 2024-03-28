# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getNumber(self, l: Optional[ListNode]) -> int:
        result = 0
        decimal_multiplier = 1
        while l.next != None:
            result += decimal_multiplier * l.val
            decimal_multiplier *= 10
            l = l.next
        result += decimal_multiplier * l.val
        return result

    def getList(self, number: int) -> ListNode:
        head = ListNode()
        tail = head
        tail.val = number % 10
        while (number >= 10):
            number //= 10
            item = ListNode(number % 10)
            tail.next = item
            tail = item
        return head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_ = self.getNumber(l1) + self.getNumber(l2)
        return self.getList(sum_)
