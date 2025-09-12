# 给你一个满足下述两条属性的mxn整数矩阵：
#
# 每行中的整数从左到右按非严格递增顺序排列。每行的第一个整数大于前一行的最后一个整数。
# 给你一个整数target ，如果target在矩阵中，返回true ；否则，返回false 。
#
#
#
# 示例
# 1：
#
#
# 输入：matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 3
# 输出：true
# 示例
# 2：
#
#
# 输入：matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 13
# 输出：false

# 最佳方式是z字形搜索
# 两次二分，先确定行，再确定列
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        if matrix[0][0] > target or matrix[len(matrix) - 1][len(matrix[0]) - 1] < target:
            return False

        h, w = len(matrix), len(matrix[0])
        row_num = -1
        for i in range(h - 1):
            if matrix[i][0] <= target < matrix[i + 1][0]:
                row_num = i
                break

        if row_num == -1:
            row_num = h - 1

        nums = matrix[row_num]
        i, j = 0, w - 1

        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1

        return False
