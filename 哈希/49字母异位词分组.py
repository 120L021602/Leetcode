# 给你一个字符串数组，请你将字母异位词组合在一起。可以按任意顺序返回结果列表。
#
#
# 示例
# 1:
#
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
#
# 输出: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
#
# 解释：
#
# 在
# strs
# 中没有字符串可以通过重新排列来形成
# "bat"。
# 字符串
# "nat"
# 和
# "tan"
# 是字母异位词，因为它们可以重新排列以形成彼此。
# 字符串
# "ate" ，"eat"
# 和
# "tea"
# 是字母异位词，因为它们可以重新排列以形成彼此。
# 示例
# 2:
#
# 输入: strs = [""]
#
# 输出: [[""]]
#
# 示例
# 3:
#
# 输入: strs = ["a"]
#
# 输出: [["a"]]
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 用哈希表来记录每个字母组合对应的异位词，最后返回所有的value
        hash_map = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in hash_map:
                hash_map[key] = [s]
            else:
                hash_map[key].append(s)

        return list(hash_map.values())





