# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        l = len(columnTitle)
        columnTitle = columnTitle.lower()
        ans = 0
        for i in range(l, 0, -1):
            b_26 = pow(26,l-i)
            ans = ans + (ord(columnTitle[i-1]) - 96)*b_26
        return ans
  
