# 在给定的
# m
# x
# n
# 网格
# grid
# 中，每个单元格可以有以下三个值之一：
#
# 值
# 0
# 代表空单元格；
# 值
# 1
# 代表新鲜橘子；
# 值
# 2
# 代表腐烂的橘子。
# 每分钟，腐烂的橘子
# 周围
# 4
# 个方向上相邻
# 的新鲜橘子都会腐烂。
#
# 返回
# 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 - 1 。
#
#
#
# 示例
# 1：
#
#
#
# 输入：grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
# 输出：4
# 示例
# 2：
#
# 输入：grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
# 输出：-1
# 解释：左下角的橘子（第
# 2
# 行， 第
# 0
# 列）永远不会腐烂，因为腐烂只会发生在
# 4
# 个方向上。
# 示例
# 3：
#
# 输入：grid = [[0, 2]]
# 输出：0
# 解释：因为
# 0
# 分钟时已经没有新鲜橘子了，所以答案就是
# 0 。


from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        queue = deque()

        # 1. 收集所有腐烂橘子的位置 & 统计新鲜橘子数量
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # 没有新鲜橘子，直接返回 0
        if fresh == 0:
            return 0

        minutes = -1  # 初始为 -1，第一轮 BFS 后变成 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # 2. 开始 BFS 扩散腐烂
        while queue:
            minutes += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # 如果相邻是新鲜橘子，就腐烂它
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        queue.append((nx, ny))

        # 3. 看是否还有新鲜橘子
        return minutes if fresh == 0 else -1