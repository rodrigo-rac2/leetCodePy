# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        resp = [[1]]
        if numRows == 1: return resp
        resp.append([1, 1])
        currentRow = 2
        while currentRow < numRows:
            currentRow += 1
            row = []
            row.append(1)
            for i in range(len(resp[-1]) - 1):
                row.append(resp[-1][i] + resp[-1][i+1])
            row.append(1)
            resp.append(row)
        return resp
