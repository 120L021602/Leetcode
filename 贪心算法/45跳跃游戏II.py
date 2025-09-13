# 给定一个长度为
# n
# 的
# 0
# 索引整数数组
# nums。初始位置在下标
# 0。
#
# 每个元素
# nums[i]
# 表示从索引
# i
# 向后跳转的最大长度。换句话说，如果你在索引
# i
# 处，你可以跳转到任意(i + j)
# 处：
#
# 0 <= j <= nums[i]
# 且
# i + j < n
# 返回到达
# n - 1
# 的最小跳跃次数。测试用例保证可以到达
# n - 1。
#
#
#
# 示例
# 1:
#
# 输入: nums = [2, 3, 1, 1, 4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是
# 2。
# 从下标为
# 0
# 跳到下标为
# 1
# 的位置，跳
# 1
# 步，然后跳
# 3
# 步到达数组的最后一个位置。
# 示例
# 2:
#
# 输入: nums = [2, 3, 0, 1, 4]
# 输出: 2


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        curEnd = 0
        furthest = 0
        n = len(nums)

        for i in range(n - 1):
            furthest = max(i + nums[i], furthest)
            if curEnd == i:
                jumps += 1
                curEnd = furthest

        return jumps
