# 给你一个整数数组nums和一个整数k ，请你统计并返回
# 该数组中和为k的子数组的个数 。
#
# 子数组是数组中元素的连续非空序列。
#
#
#
# 示例
# 1：
#
# 输入：nums = [1, 1, 1], k = 2
# 输出：2
# 示例
# 2：
#
# 输入：nums = [1, 2, 3], k = 3
# 输出：2


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 字典记录前缀和出现的次数
        prefix_count = {0: 1}
        prefix_sum = 0
        res = 0

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix_count:
                res += prefix_count[prefix_sum - k]
            if prefix_sum not in prefix_count:
                prefix_count[prefix_sum] = 1
            else:
                prefix_count[prefix_sum] += 1

        return res