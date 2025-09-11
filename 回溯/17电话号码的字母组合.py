# 给定一个仅包含数字2 - 9的字符串，返回所有它能表示的字母组合。答案可以按任意顺序返回。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意1不对应任何字母。
#
#
#
#
#
# 示例
# 1：
#
# 输入：digits = "23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
# 示例
# 2：
#
# 输入：digits = ""
# 输出：[]
# 示例
# 3：
#
# 输入：digits = "2"
# 输出：["a", "b", "c"]


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        path = []
        self.backtracking(phoneMap, digits, 0, path, res)
        return res

    def backtracking(self, phoneMap, digits, startIndex, path, res):
        if len(path) == len(digits):
            res.append("".join(path))
            return

        curLetters = phoneMap[digits[startIndex]]
        for letter in curLetters:
            path.append(letter)
            self.backtracking(phoneMap, digits, startIndex + 1, path, res)
            path.pop()