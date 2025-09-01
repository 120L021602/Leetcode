# 给你一个整数数组nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的
# k个数字。滑动窗口每次只向右移动一位。
#
# 返回滑动窗口中的最大值 。
import collections


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k == 0:
            return []

        dq = collections.deque()
        res = []
        n = len(nums)

        for i in range(n):
            # 移除队尾比当前值小的元素
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()

            dq.append(i)

            # 移除不在窗口内的索引
            if dq[0] <= i - k:
                dq.popleft()

            # 添加窗口最大值到结果
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res


