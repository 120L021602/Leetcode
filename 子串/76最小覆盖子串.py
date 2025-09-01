# 给你一个字符串s 、一个字符串t 。返回s中涵盖t所有字符的最小子串。如果
# s中不存在涵盖t所有字符的子串，则返回空字符串"" 。
#
#
#
# 注意：对于t中重复字符，我们寻找的子字符串中该字符数量必须不少于
# t中该字符数量。如果s中存在这样的子串，我们保证它是唯一的答案。
#
#
# 示例
# 1：
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串
# "BANC"
# 包含来自字符串
# t
# 的
# 'A'、'B'
# 和
# 'C'。
# 示例
# 2：
#
# 输入：s = "a", t = "a"
# 输出："a"
# 解释：整个字符串
# s
# 是最小覆盖子串。
# 示例
# 3:
#
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t
# 中两个字符
# 'a'
# 均应包含在
# s
# 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 核心思路如下：
        # 统计 t 中每个字符的频率，保存在 need 哈希表中。
        # 使用一个滑动窗口 [left, right] 维护窗口内字符的频率 window。
        # 移动右指针 right，扩张窗口，直到窗口包含 t 所需所有字符。
        # 然后移动左指针 left，尝试收缩窗口，直到窗口不再满足条件。
        # 在这个过程中记录最小长度以及对应的起始下标。

        if not s or not t:
            return ""

        need = {}
        for c in t:
            if c not in need:
                need[c] = 1
            else:
                need[c] += 1

        window = {}        # 当前窗口中的字符频率
        left = 0
        right = 0
        valid = 0          # 当前满足条件的字符数
        start = 0          # 最小覆盖子串的起始索引
        min_len = float("inf")  # 最小长度
        n = len(s)

        while right < n:
            c = s[right]
            right += 1

            # 更新窗口内数据
            if c in need:
                if c not in window:
                    window[c] = 1
                else:
                    window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # 尝试收缩左侧窗口
            while valid == len(need):
                if min_len > right - left:
                    min_len = right - left
                    start = left

                d = s[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return "" if min_len == float("inf") else s[start: start + min_len]