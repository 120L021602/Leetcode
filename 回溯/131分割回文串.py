# 给你一个字符串s，请你将s分割成一些子串，使每个子串都是回文串 。返回s所有可能的分割方案。
#
#
#
# 示例
# 1：
#
# 输入：s = "aab"
# 输出：[["a", "a", "b"], ["aa", "b"]]
# 示例
# 2：
#
# 输入：s = "a"
# 输出：[["a"]]


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        path, res = [], []
        start_index = 0
        self.backtracking(s, start_index, path, res)
        return res

    def backtracking(self, s, start_index, path, res):
        if start_index == len(s):
            res.append(path[:])
            return

        for i in range(start_index, len(s)):
            if self.is_huiwen(s[start_index: i + 1]):
                path.append(s[start_index: i + 1])
                self.backtracking(s, i + 1, path, res)
                path.pop()

    def is_huiwen(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True