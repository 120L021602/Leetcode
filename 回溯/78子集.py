# 给你一个整数数组nums ，数组中的元素互不相同 。返回该数组所有可能的子集（幂集）。
#
# 解集不能包含重复的子集。你可以按任意顺序返回解集。
#
#
#
# 示例
# 1：
#
# 输入：nums = [1, 2, 3]
# 输出：[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
# 示例
# 2：
#
# 输入：nums = [0]
# 输出：[[], [0]]
from typing import List


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        start_index = 0
        path = []
        nums.sort()
        n = len(nums)
        self.backtracking(nums, start_index, path, res, n)
        return res

    def backtracking(self, nums, start_index, path, res, n):
        res.append(path[:])

        for i in range(start_index, n):
            path.append(nums[i])
            self.backtracking(nums, i + 1, path, res, n)
            path.pop()
