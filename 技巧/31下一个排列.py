# 整数数组的一个
# 排列
# 就是将其所有成员以序列或线性顺序排列。
#
# 例如，arr = [1, 2, 3] ，以下这些都可以视作
# arr
# 的排列：[1, 2, 3]、[1, 3, 2]、[3, 1, 2]、[2, 3, 1] 。
# 整数数组的
# 下一个排列
# 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的
# 下一个排列
# 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。
#
# 例如，arr = [1, 2, 3]
# 的下一个排列是[1, 3, 2] 。
# 类似地，arr = [2, 3, 1]
# 的下一个排列是[3, 1, 2] 。
# 而
# arr = [3, 2, 1]
# 的下一个排列是[1, 2, 3] ，因为[3, 2, 1]
# 不存在一个字典序更大的排列。
# 给你一个整数数组
# nums ，找出
# nums
# 的下一个排列。
#
# 必须
# 原地
# 修改，只允许使用额外常数空间。
#
#
#
# 示例
# 1：
#
# 输入：nums = [1, 2, 3]
# 输出：[1, 3, 2]
# 示例
# 2：
#
# 输入：nums = [3, 2, 1]
# 输出：[1, 2, 3]
# 示例
# 3：
#
# 输入：nums = [1, 1, 5]
# 输出：[1, 5, 1]


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 从右向左找到第一个下降的位置 i，使得 nums[i] < nums[i+1]
        n = len(nums)
        pos_1 = -1

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pos_1 = i
                break

        # 再从右向左找到第一个比 nums[i] 大的元素 j，交换它们
        if pos_1 >= 0:
            for i in range(n - 1, -1, -1):
                if nums[i] > nums[pos_1]:
                    nums[i], nums[pos_1] = nums[pos_1], nums[i]
                    break

        # 最后，将下标 i+1 到末尾的部分反转，变为最小序列
        left, right = pos_1 + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1