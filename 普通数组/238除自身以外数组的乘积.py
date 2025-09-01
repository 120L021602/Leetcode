# 给你一个整数数组nums，返回数组answer ，其中answer[i]等于nums中除nums[i]之外其余各元素的乘积 。
# 题目数据保证数组nums之中任意元素的全部前缀元素和后缀的乘积都在32位整数范围内。
#
# 请不要使用除法，且在O(n)时间复杂度内完成此题。
#
#
#
# 示例
# 1:
#
# 输入: nums = [1, 2, 3, 4]
# 输出: [24, 12, 8, 6]
# 示例
# 2:
#
# 输入: nums = [-1, 1, 0, -3, 3]
# 输出: [0, 0, 9, 0, 0]
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 先遍历一遍 nums，从左往右，构建前缀积数组。
        # 再从右往左遍历 nums，与前缀积相乘，得到答案数组。
        n = len(nums)
        prefix_amass = [1] * n
        ans = [0] * n
        cur_amass = 1

        for i in range(n):
            prefix_amass[i] = cur_amass
            cur_amass *= nums[i]

        cur_amass = 1
        for i in range(n - 1, -1, -1):
            ans[i] = cur_amass * prefix_amass[i]
            cur_amass *= nums[i]

        return ans