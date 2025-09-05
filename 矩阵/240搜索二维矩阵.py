# 编写一个高效的算法来搜索mxn矩阵matrix中的一个目标值target 。该矩阵具有以下特性：
#
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
#
#
# 示例
# 1：
#
#
# 输入：matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
#                [18, 21, 23, 26, 30]], target = 5
# 输出：true
# 示例
# 2：
#
#
# 输入：matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
#                [18, 21, 23, 26, 30]], target = 20
# 输出：false


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 从右上角开始查找
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1

        while 0 <= i <= m - 1 and 0 <= j <= n - 1:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1

        return False
