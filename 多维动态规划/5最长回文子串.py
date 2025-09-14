# 给你一个字符串s，找到s中最长的回文子串。
#
#
#
# 示例
# 1：
#
# 输入：s = "babad"
# 输出："bab"
# 解释："aba"
# 同样是符合题意的答案。
# 示例
# 2：
#
# 输入：s = "cbbd"
# 输出："bb"


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n < 2:
            return s

        max_len = 1
        start = 0
        dp = [[False] * n for _ in range(n)]

        for j in range(1, n):
            for i in range(j):
                if s[j] == s[i]:
                    if j - i <= 2:
                        dp[i][j] = True
                    else:
                        if dp[i + 1][j - 1]:
                            dp[i][j] = True

                if dp[i][j] and (j - i + 1) > max_len:
                    max_len = j - i + 1
                    start = i

        return s[start: start + max_len]