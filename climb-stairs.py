# problem: https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: 
            return 1
        elif n == 2:
            return 2
        first = 0
        second = 1
        next = 0
        for i in range(n):
            next = first + second
            first = second
            second = next
        return next
