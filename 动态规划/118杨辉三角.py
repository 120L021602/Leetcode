# 给定一个非负整数numRows，生成「杨辉三角」的前numRows行。
#
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
#
#
#
#
#
# 示例
# 1:
#
# 输入: numRows = 5
# 输出: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
# 示例
# 2:
#
# 输入: numRows = 1
# 输出: [[1]]


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        path = []

        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1], [1, 1]]

        res = [[1], [1, 1]]

        for i in range(3, numRows + 1):
            path = [0] * i
            path[0], path[-1] = 1, 1
            for j in range(1, i - 1):
                path[j] = res[-1][j - 1] + res[-1][j]
            res.append(path)

        return res