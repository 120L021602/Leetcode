# 给你一个未排序的整数数组nums ，请你找出其中没有出现的最小的正整数。
#
# 请你实现时间复杂度为O(n)并且只使用常数级别额外空间的解决方案。
#
#
# 示例
# 1：
#
# 输入：nums = [1, 2, 0]
# 输出：3
# 解释：范围[1, 2]
# 中的数字都在数组中。
# 示例
# 2：
#
# 输入：nums = [3, 4, -1, 1]
# 输出：2
# 解释：1
# 在数组中，但
# 2
# 没有。
# 示例
# 3：
#
# 输入：nums = [7, 8, 9, 11, 12]
# 输出：1
# 解释：最小的正数
# 1
# 没有出现。


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 遍历整个数组，把所有 在 [1, n] 范围内的数 nums[i]，放到它应该在的位置上：nums[nums[i] - 1]。
        # 再次遍历数组，如果 nums[i] != i + 1，说明 i + 1 就是最小缺失的正整数。
        # 都匹配上了？说明缺失的是 n + 1。
        n = len(nums)

        for i in range(n):
            # 这里是while而不是if，因为交换了一次之后可能要接着换
            while 1 <= nums[i] <= n:
                target = nums[i] - 1
                if nums[target] == nums[i]:
                    break  # 避免死循环（重复值）
                nums[i], nums[target] = nums[target], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
