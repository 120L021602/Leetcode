# 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
# n皇后问题研究的是如何将n个皇后放置在n×n的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 给你一个整数n ，返回所有不同的n皇后问题的解决方案。
#
# 每一种解法包含一个不同的n的棋子放置方案，该方案中'Q'和'.'分别代表了皇后和空位。
#
#
#
# 示例
# 1：
#
#
# 输入：n = 4
# 输出：[[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
# 解释：如上图所示，4
# 皇后问题存在两个不同的解法。
# 示例
# 2：
#
# 输入：n = 1
# 输出：[["Q"]]


class Solution:
    def solveNQueens(self, n):
        # 初始化结果集
        res = []
        # 初始化棋盘，开始时全部是空位 '.'
        board = [['.' for _ in range(n)] for _ in range(n)]
        # 初始化三个集合，用于快速判断位置是否合法
        cols = set()
        diag1 = set() # 正对角线：row - col
        diag2 = set() # 反对角线：row + col

        # 定义回溯函数
        def backtrack(row):
            # 终止条件：所有行都成功放置了皇后
            if row == n:
                # 将当前棋盘转换为题目要求的格式（每一行是一个字符串）
                solution = [''.join(r) for r in board]
                res.append(solution)
                return

            # 遍历当前行(row)的所有列
            for col in range(n):
                # 计算当前位置的两个对角线标识
                d1 = row - col
                d2 = row + col
                # 检查当前位置是否合法
                if col in cols or d1 in diag1 or d2 in diag2:
                    continue # 不合法，跳过当前列

                # 做出选择：放置皇后
                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(d1)
                diag2.add(d2)

                # 递归进入下一行
                backtrack(row + 1)

                # 撤销选择：回溯，移除皇后
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(d1)
                diag2.remove(d2)

        # 从第0行开始回溯
        backtrack(0)
        return res


