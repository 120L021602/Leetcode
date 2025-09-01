# 以数组intervals表示若干个区间的集合，其中单个区间为intervals[i] = [starti, endi] 。
# 请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
#
#
#
# 示例
# 1：
#
# 输入：intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# 输出：[[1, 6], [8, 10], [15, 18]]
# 解释：区间[1, 3]
# 和[2, 6]
# 重叠, 将它们合并为[1, 6].
# 示例
# 2：
#
# 输入：intervals = [[1, 4], [4, 5]]
# 输出：[[1, 5]]
# 解释：区间[1, 4]
# 和[4, 5]
# 可被视为重叠区间。
# 示例
# 3：
#
# 输入：intervals = [[4, 7], [1, 4]]
# 输出：[[1, 7]]
# 解释：区间[1, 4]
# 和[4, 7]
# 可被视为重叠区间。
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        n = len(intervals)

        for i in range(1, n):
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])

        return res



