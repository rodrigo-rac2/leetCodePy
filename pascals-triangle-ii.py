# https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]
        pascal_triangle = [[1], [1, 1]]
        for i in range(1, rowIndex):
            row = [1]
            for j in range(len(pascal_triangle[-1]) - 1):
                row.append(pascal_triangle[-1][j] + pascal_triangle[-1][j+1])
            row.append(1)
            pascal_triangle.append(row)
        return pascal_triangle[-1]
