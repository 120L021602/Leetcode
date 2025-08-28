# 给定一个数组nums，编写一个函数将所有0移动到数组的末尾，同时保持非零元素的相对顺序。
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
#
#
#
# 示例
# 1:
#
# 输入: nums = [0, 1, 0, 3, 12]
# 输出: [1, 3, 12, 0, 0]
# 示例
# 2:
#
# 输入: nums = [0]
# 输出: [0]


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 两个指针，指针i代表当前要存放非零数字的位置，指针j代表当前探索的位置
        i, j = 0, 0
        n = len(nums)
        while j < n:
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
                j += 1
            else:
                j += 1
        # 将位置i后面的元素全部设置为0即可
        while i < n:
            nums[i] = 0
            i += 1
