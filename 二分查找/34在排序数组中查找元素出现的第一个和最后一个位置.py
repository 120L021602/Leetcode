# 给你一个按照非递减顺序排列的整数数组nums，和一个目标值target。请你找出给定目标值在数组中的开始位置和结束位置。
#
# 如果数组中不存在目标值target，返回[-1, -1]。
#
# 你必须设计并实现时间复杂度为O(logn) 的算法解决此问题。
#
#
#
# 示例
# 1：
#
# 输入：nums = [5, 7, 7, 8, 8, 10], target = 8
# 输出：[3, 4]
# 示例
# 2：
#
# 输入：nums = [5, 7, 7, 8, 8, 10], target = 6
# 输出：[-1, -1]
# 示例
# 3：
#
# 输入：nums = [], target = 0
# 输出：[-1, -1]


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        left, right = self.findLeft(nums, target), self.findRight(nums, target)
        return [left, right]

    def findLeft(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if 0 <= left < len(nums) and nums[left] == target:
            return left
        return -1

    def findRight(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if 0 <= right < len(nums) and nums[right] == target:
            return right
        return -1