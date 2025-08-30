# 给定n个非负整数表示每个宽度为1的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 示例
# 1：
#
#
#
# 输入：height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# 输出：6
# 解释：上面是由数组[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# 表示的高度图，在这种情况下，可以接
# 6
# 个单位的雨水（蓝色部分表示雨水）。
# 示例
# 2：
#
# 输入：height = [4, 2, 0, 3, 2, 5]
# 输出：9


import collections
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 单调递减栈，栈中存放下标
        n = len(height)
        _sum = 0
        stack = collections.deque()
        stack.append(0)

        for i in range(1, n):
            # 小于栈顶，直接压入
            if height[i] < height[stack[-1]]:
                stack.append(i)

            # 等于栈顶，替换栈顶（更新为当前下标），以保证最右边的柱子下标存入栈中
            elif height[i] == height[stack[-1]]:
                stack.pop()
                stack.append(i)

            # 当前柱子比栈顶高，说明有可能构成一个“凹槽”；
            # 弹出中间的柱子 mid，将其作为接水的“底部”；
            # 判断栈是否为空（**必须判断！**否则 stack[-1] 越界）；
            # 如果不为空，说明有左边界 + 当前柱子作为右边界；
            # 算法：
            # 高度 = min(左边界, 右边界) - 底部高度
            # 宽度 = 右边下标 - 左边下标 - 1
            # 面积 = 高 × 宽，即为接水量；
            # 更新 _sum。
            # 最后把当前下标也入栈。
            else:
                while stack and height[i] > height[stack[-1]]:
                    mid = stack[-1]
                    stack.pop()
                    if stack:
                        h = min(height[i], height[stack[-1]]) - height[mid]
                        w = i - stack[-1] - 1
                        cur_sum = h * w
                        _sum += cur_sum
                stack.append(i)

        return _sum
