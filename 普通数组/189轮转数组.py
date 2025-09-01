# 给定一个整数数组nums，将数组中的元素向右轮转k个位置，其中k是非负数。
#
#
#
# 示例
# 1:
#
# 输入: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
# 输出: [5, 6, 7, 1, 2, 3, 4]
# 解释:
# 向右轮转
# 1
# 步: [7, 1, 2, 3, 4, 5, 6]
# 向右轮转
# 2
# 步: [6, 7, 1, 2, 3, 4, 5]
# 向右轮转
# 3
# 步: [5, 6, 7, 1, 2, 3, 4]
# 示例
# 2:
#
# 输入：nums = [-1, -100, 3, 99], k = 2
# 输出：[3, 99, -1, -100]
# 解释:
# 向右轮转
# 1
# 步: [99, -1, -100, 3]
# 向右轮转
# 2
# 步: [3, 99, -1, -100]


from typing import List


class Solution:
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 三次翻转
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        # print(nums)
        self.reverse(nums, 0, k - 1)
        # print(nums)
        self.reverse(nums, k, n - 1)
