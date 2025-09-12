# 给定一个整数数组temperatures ，表示每天的温度，返回一个数组answer ，其中answer[i]是指对于第i天，下一个更高温度出现在几天后。
# 如果气温在这之后都不会升高，请在该位置用0来代替。
#
#
#
# 示例
# 1:
#
# 输入: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# 输出: [1, 1, 4, 2, 1, 1, 0, 0]
# 示例
# 2:
#
# 输入: temperatures = [30, 40, 50, 60]
# 输出: [1, 1, 1, 0]
# 示例
# 3:
#
# 输入: temperatures = [30, 60, 90]
# 输出: [1, 1, 0]
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 单调递减栈
        if not temperatures:
            return []

        stack = []
        n = len(temperatures)
        answer = [0] * n

        for i in range(n):
            if not stack or temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            while stack and temperatures[i] > temperatures[stack[-1]]:
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return answer