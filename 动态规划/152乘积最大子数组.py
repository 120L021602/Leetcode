# 给你一个整数数组nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
#
# 测试用例的答案是一个32 - 位整数。
#
#
#
# 示例
# 1:
#
# 输入: nums = [2, 3, -2, 4]
# 输出: 6
# 解释: 子数组[2, 3]
# 有最大乘积
# 6。
# 示例
# 2:
#
# 输入: nums = [-2, 0, -1]
# 输出: 0
# 解释: 结果不能为
# 2, 因为[-2, -1]
# 不是子数组。


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i]代表以nums[i]结尾的乘积最大的非空连续子数组的乘积
        n = len(nums)
        dp_max = [float("-inf")] * n
        dp_min = [float("inf")] * n
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]

        for j in range(1, n):
            if nums[j] > 0:
                dp_max[j] = max(nums[j], nums[j] * dp_max[j - 1])
                dp_min[j] = min(nums[j], nums[j] * dp_min[j - 1])
            elif nums[j] < 0:
                dp_max[j] = max(nums[j], nums[j] * dp_min[j - 1])
                dp_min[j] = min(nums[j], nums[j] * dp_max[j - 1])
            else:
                dp_max[j] = 0
                dp_min[j] = 0

        return max(dp_max)
