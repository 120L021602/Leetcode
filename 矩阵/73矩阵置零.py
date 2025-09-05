# 给定一个mxn的矩阵，如果一个元素为0 ，则将其所在行和列的所有元素都设为0 。请使用原地算法。
#
#
#
# 示例
# 1：
#
#
# 输入：matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# 输出：[[1, 0, 1], [0, 0, 0], [1, 0, 1]]
# 示例
# 2：
#
#
# 输入：matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
# 输出：[[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        m, n = [False] * row, [False] * col

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    m[i], n[j] = True, True

        for i in range(row):
            for j in range(col):
                if m[i] or n[j]:
                    matrix[i][j] = 0