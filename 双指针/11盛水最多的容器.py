# 给定一个长度为n的整数数组height 。有n条垂线，第i条线的两个端点是(i, 0)和(i, height[i]) 。
#
# 找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。返回容器可以储存的最大水量。
#
# 说明：你不能倾斜容器。
#
#
#
# 示例
# 1：
#
#
#
# 输入：[1, 8, 6, 2, 5, 4, 8, 3, 7]
# 输出：49
# 解释：图中垂直线代表输入数组[1, 8, 6, 2, 5, 4, 8, 3, 7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为
# 49。
# 示例
# 2：
#
# 输入：height = [1, 1]
# 输出：1


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n - 1
        max_volumn = 0
        while i < j:
            cur_volumn = min(height[i], height[j]) * (j - i)
            max_volumn = max(max_volumn, cur_volumn)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_volumn