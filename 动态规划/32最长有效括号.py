# 给你一个只包含'('和')'的字符串，找出最长有效（格式正确且连续）括号子串的长度。
#
# 左右括号匹配，即每个左括号都有对应的右括号将其闭合的字符串是格式正确的，比如"(()())"。
#
#
#
# 示例
# 1：
#
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是
# "()"
# 示例
# 2：
#
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是
# "()()"
# 示例
# 3：
#
# 输入：s = ""
# 输出：0


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 用栈来追踪括号匹配的位置。我们将不匹配的位置记录下来，然后计算最长的连续有效区间长度。
        stack = [-1]
        max_len = 0
        n = len(s)

        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len