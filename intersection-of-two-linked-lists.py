# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def getNodeLen(list):
    length = 1
    while list.next is not None:
        length = length + 1
        list = list.next
    return length

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = getNodeLen(headA)
        lenB = getNodeLen(headB)
        if(lenA > lenB):
            while lenA > lenB: 
                headA = headA.next
                lenA = lenA - 1
        else:
            while lenB > lenA: 
                headB = headB.next
                lenB = lenB - 1
        returnL = headA
        while headA is not None and headB is not None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
