# 给你一个无重复元素的整数数组candidates和一个目标整数target ，找出candidates
# 中可以使数字和为目标数target的所有不同组合 ，并以列表形式返回。你可以按任意顺序返回这些组合。
#
# candidates中的同一个数字可以无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。
#
# 对于给定的输入，保证和为target的不同组合数少于150个。
#
#
#
# 示例
# 1：
#
# 输入：candidates = [2, 3, 6, 7], target = 7
# 输出：[[2, 2, 3], [7]]
# 解释：
# 2
# 和
# 3
# 可以形成一组候选，2 + 2 + 3 = 7 。注意
# 2
# 可以使用多次。
# 7
# 也是一个候选， 7 = 7 。
# 仅有这两种组合。
# 示例
# 2：
#
# 输入: candidates = [2, 3, 5], target = 8
# 输出: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
# 示例
# 3：
#
# 输入: candidates = [2], target = 1
# 输出: []


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, path = [], []
        start_index = 0
        candidates.sort()
        self.backtracking(candidates, target, start_index, path, res)
        return res

    def backtracking(self, nums, target, start_index, path, res):
        if sum(path) == target:
            res.append(path[:])
            return

        elif sum(path) > target:
            return

        for i in range(start_index, len(nums)):
            path.append(nums[i])
            self.backtracking(nums, target, i, path, res)
            path.pop()
