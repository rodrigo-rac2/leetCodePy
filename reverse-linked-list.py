# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = None
        current = head
        while current:
            next_n = current.next
            current.next = answer
            answer = current
            current = next_n
        
        return answer
Ï
        # Solution 2
        # if not head: return head
        # answer_l = []
        # while head:
        #     answer_l.append(head.val)
        #     head = head.next
        # answer = ListNode()
        # runner = answer
        # answer_l = answer_l[::-1]
        # for i in range(len(answer_l)):
        #     runner.val = answer_l[i]
        #     if i < len(answer_l) - 1:
        #         runner.next = ListNode()
        #         runner = runner.next
        # return answer
        
        # Solution 3:
        # answer_l = []
        # current = head
        # while (current):
        #     answer_l.append(current.val)
        #     current = current.next
        # answer = ListNode()
        # answer_h = answer
        # length = len(answer_l)
        # for i in range(length):
        #     answer.val = answer_l[length - 1 - i]
        #     if i < length - 1:
        #         answer.next = ListNode()
        #         answer = answer.next
        # return answer_h
