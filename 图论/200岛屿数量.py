# 给你一个由'1'（陆地）和'0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和 / 或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
#
#
#
# 示例
# 1：
#
# 输入：grid = [
#     ['1', '1', '1', '1', '0'],
#     ['1', '1', '0', '1', '0'],
#     ['1', '1', '0', '0', '0'],
#     ['0', '0', '0', '0', '0']
# ]
# 输出：1
# 示例
# 2：
#
# 输入：grid = [
#     ['1', '1', '0', '0', '0'],
#     ['1', '1', '0', '0', '0'],
#     ['0', '0', '1', '0', '0'],
#     ['0', '0', '0', '1', '1']
# ]
# 输出：3


# 深搜，搜索的过程中把“1”修改成“0”
class Solution:
    def dfs(self, i, j, grid, h, w):
        grid[i][j] = "0"
        for (x, y) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= x <= h - 1 and 0 <= y <= w - 1 and grid[x][y] == "1":
                self.dfs(x, y, grid, h, w)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        h, w = len(grid), len(grid[0])
        cnt = 0

        for i in range(h):
            for j in range(w):
                if grid[i][j] == "1":
                    cnt += 1
                    self.dfs(i, j, grid, h, w)

        return cnt