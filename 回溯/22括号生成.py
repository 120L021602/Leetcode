# 数字n代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合。
#
#
#
# 示例
# 1：
#
# 输入：n = 3
# 输出：["((()))", "(()())", "(())()", "()(())", "()()()"]
# 示例
# 2：
#
# 输入：n = 1
# 输出：["()"]


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        path, res = [], []
        leftCnt, rightCnt = 0, 0
        self.backtracking(n, leftCnt, rightCnt, path, res)
        return res

    def backtracking(self, n, leftCnt, rightCnt, path, res):
        # 注意这里是2*n
        if len(path) == 2 * n:
            res.append("".join(path))
            return

        if leftCnt < n:
            path.append("(")
            self.backtracking(n, leftCnt + 1, rightCnt, path, res)
            path.pop()

        if rightCnt < leftCnt:
            path.append(")")
            self.backtracking(n, leftCnt, rightCnt + 1, path, res)
            path.pop()
