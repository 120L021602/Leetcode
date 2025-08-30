# 给定两个字符串s和p，找到s中所有p的异位词的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
#
#
#
# 示例
# 1:
#
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0, 6]
# 解释:
# 起始索引等于
# 0
# 的子串是
# "cba", 它是
# "abc"
# 的异位词。
# 起始索引等于
# 6
# 的子串是
# "bac", 它是
# "abc"
# 的异位词。
# 示例
# 2:
#
# 输入: s = "abab", p = "ab"
# 输出: [0, 1, 2]
# 解释:
# 起始索引等于
# 0
# 的子串是
# "ab", 它是
# "ab"
# 的异位词。
# 起始索引等于
# 1
# 的子串是
# "ba", 它是
# "ab"
# 的异位词。
# 起始索引等于
# 2
# 的子串是
# "ab", 它是
# "ab"
# 的异位词。
#
#
# 提示:
#
# 1 <= s.length, p.length <= 3 * 104
# s和p仅包含小写字母


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # 获取两个字符串的长度
        s_len, p_len = len(s), len(p)

        # 如果主串长度小于模式串，不可能有异位词，直接返回空列表
        if s_len < p_len:
            return []

        # 保存结果（所有异位词的起始下标）
        res = []

        # 初始化两个长度为 26 的数组，分别记录字符频率（a-z）
        s_count = [0] * 26  # 当前窗口字符频率
        p_count = [0] * 26  # 模式串字符频率

        # 构建初始窗口和 p 的频率统计
        for i in range(p_len):
            s_count[ord(s[i]) - ord("a")] += 1  # 窗口中第 i 个字符频率加一
            p_count[ord(p[i]) - ord("a")] += 1  # 模式串中第 i 个字符频率加一

        # 如果初始窗口和模式串频率完全一样，说明是一个异位词
        if s_count == p_count:
            res.append(0)

        # 滑动窗口：从索引 1 开始滑动窗口（总共 s_len - p_len 次）
        for i in range(s_len - p_len):
            # 移除窗口最左侧字符的频率（出窗口）
            s_count[ord(s[i]) - ord("a")] -= 1
            # 添加窗口最右侧新字符的频率（进窗口）
            s_count[ord(s[i + p_len]) - ord("a")] += 1
            # 判断当前窗口是否和 p 的频率相同
            if s_count == p_count:
                # 如果相同，说明是异位词，记录起始索引 i + 1
                res.append(i + 1)

        # 返回所有异位词的起始索引
        return res