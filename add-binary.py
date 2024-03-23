# https://leetcode.com/problems/add-binary/

class Solution:
    def binaryToDecimal(self, n: str) -> int:
        return int(n,2)
        # result = 0
        # for i in range(len(n)-1,-1,-1):
        #     result += int(n[i]) * pow(2,len(n)-1-i)
        # return result
    
    def decimalToBinary(self, n: int) -> str:
        return bin(n)[2:]
        # if n == 0:
        #     return "0"
        # result = []
        # while n > 0:
        #     result.insert(0, str(n % 2))
        #     n //= 2
        # return ''.join(result)


    def addBinary(self, a: str, b: str) -> str:
        d_sum = self.binaryToDecimal(a) + self.binaryToDecimal(b)
        return self.decimalToBinary(d_sum)
        
