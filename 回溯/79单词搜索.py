# 给定一个xn二维字符网格board和一个字符串单词word 。如果word存在于网格中，返回true ；否则，返回false 。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#
#
# 示例
# 1：
#
#
# 输入：board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], word = "ABCCED"
# 输出：true
# 示例
# 2：
#
#
# 输入：board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], word = "SEE"
# 输出：true
# 示例
# 3：
#
#
# 输入：board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], word = "ABCB"
# 输出：false


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False

        visited = set()
        h = len(board)
        w = len(board[0])

        for i in range(h):
            for j in range(w):
                if self.check(board, word, i, j, 0, visited, h, w):
                    return True

        return False

    def check(self, board, word, i, j, k, visited, h, w):
        if board[i][j] != word[k]:
            return False

        if k + 1 == len(word):
            return True

        visited.add((i, j))
        for (x, y) in [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= x <= h - 1 and 0 <= y <= w - 1 and (x, y) not in visited:
                if self.check(board, word, x, y, k + 1, visited, h, w):
                    return True

        visited.remove((i, j))
        return False
