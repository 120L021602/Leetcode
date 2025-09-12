# 给定两个大小分别为m和n的正序（从小到大）数组nums1和nums2。请你找出并返回这两个正序数组的中位数 。
#
# 算法的时间复杂度应该为O(log(m + n)) 。
#
#
#
# 示例
# 1：
#
# 输入：nums1 = [1, 3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1, 2, 3] ，中位数
# 2
# 示例
# 2：
#
# 输入：nums1 = [1, 2], nums2 = [3, 4]
# 输出：2.50000
# 解释：合并数组 = [1, 2, 3, 4] ，中位数(2 + 3) / 2 = 2.5


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 确保 nums1 是较短的数组
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        imin, imax = 0, m
        half_len = (m + n + 1) // 2

        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i

            if i < m and nums2[j - 1] > nums1[i]:
                # i 太小了，往右移
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # i 太大了，往左移
                imax = i - 1
            else:
                # 找到合适的 i
                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left  # 奇数长度，中位数就是左边最大值

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0



