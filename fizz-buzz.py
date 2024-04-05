# https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for i in range(n):
            num = i + 1
            if num%3 == 0 and num%5 == 0: output.append("FizzBuzz")
            elif num%3 == 0: output.append("Fizz")
            elif num%5 == 0: output.append("Buzz")
            else: output.append(f"{num}")
        return output
