# 给定一个不含重复数字的数组nums ，返回其所有可能的全排列 。你可以按任意顺序返回答案。
#
#
#
# 示例
# 1：
#
# 输入：nums = [1, 2, 3]
# 输出：[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
# 示例
# 2：
#
# 输入：nums = [0, 1]
# 输出：[[0, 1], [1, 0]]
# 示例
# 3：
#
# 输入：nums = [1]
# 输出：[[1]]
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        self.backtracking(nums, path, res)
        return res

    def backtracking(self, nums, path, res):
        if len(path) == len(nums):
            res.append(path[:])

        for num in nums:
            if num not in path:
                path.append(num)
                self.backtracking(nums, path, res)
                path.pop()