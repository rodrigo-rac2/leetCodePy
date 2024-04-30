# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        answer_l = []
        current = head
        while (current):
            answer_l.append(current.val)
            current = current.next
        print(answer_l)
        answer = ListNode()
        answer_h = answer
        length = len(answer_l)
        for i in range(length):
            answer.val = answer_l[length - 1 - i]
            if i < length - 1:
                answer.next = ListNode()
                answer = answer.next
        return answer_h
