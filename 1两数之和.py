# 给定一个整数数组nums和一个整数目标值target，请你在该数组中找出和为目标值target的那两个整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
#
# 你可以按任意顺序返回答案。
#
#
#
# 示例
# 1：
#
# 输入：nums = [2, 7, 11, 15], target = 9
# 输出：[0, 1]
# 解释：因为
# nums[0] + nums[1] == 9 ，返回[0, 1] 。
# 示例
# 2：
#
# 输入：nums = [3, 2, 4], target = 6
# 输出：[1, 2]
# 示例
# 3：
#
# 输入：nums = [3, 3], target = 6
# 输出：[0, 1]


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 第一次遍历nums数组，用哈希表记录nums数组中每个元素的下标
        hash_map = {}
        n = len(nums)
        for i in range(n):
            hash_map[nums[i]] = i

        # 第二次遍历nums数组
        for i in range(n):
            tmp = target - nums[i]
            if tmp in hash_map and hash_map[tmp] != i:
                return [i, hash_map[tmp]]
