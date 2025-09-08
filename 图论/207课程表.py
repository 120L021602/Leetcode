# 你这个学期必须选修
# numCourses
# 门课程，记为
# 0
# 到
# numCourses - 1 。
#
# 在选修某些课程之前需要一些先修课程。 先修课程按数组
# prerequisites
# 给出，其中
# prerequisites[i] = [ai, bi] ，表示如果要学习课程
# ai
# 则
# 必须
# 先学习课程
# bi 。
#
# 例如，先修课程对[0, 1]
# 表示：想要学习课程
# 0 ，你需要先完成课程
# 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回
# true ；否则，返回
# false 。
#
#
#
# 示例
# 1：
#
# 输入：numCourses = 2, prerequisites = [[1, 0]]
# 输出：true
# 解释：总共有
# 2
# 门课程。学习课程
# 1
# 之前，你需要完成课程
# 0 。这是可能的。
# 示例
# 2：
#
# 输入：numCourses = 2, prerequisites = [[1, 0], [0, 1]]
# 输出：false
# 解释：总共有
# 2
# 门课程。学习课程
# 1
# 之前，你需要先完成​课程
# 0 ；并且学习课程
# 0
# 之前，你还应先完成课程
# 1 。这是不可能的。


import collections


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        判断是否能完成所有课程（是否存在有向环）

        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # 初始化每门课的入度
        indegree = [0] * numCourses

        # 构建邻接表：pre -> list of courses that depend on pre
        adj = collections.defaultdict(list)

        # 构建图和入度表
        for cur, pre in prerequisites:
            indegree[cur] += 1  # 当前课程需要一个前置课
            adj[pre].append(cur)  # pre 是 cur 的前置课

        # 初始化队列，加入所有入度为 0 的课程（可直接学习）
        queue = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # 开始 BFS 拓扑排序
        while queue:
            n = len(queue)
            for i in range(n):
                pre = queue.popleft()  # 学完一个课程
                numCourses -= 1  # 剩余课程数量减一

                # 所有依赖这个课程的后续课程
                for cur in adj[pre]:
                    indegree[cur] -= 1  # 减去一个前置课
                    if indegree[cur] == 0:
                        queue.append(cur)  # 如果入度为 0，加入队列

        # 如果所有课程都被学完，说明没有环
        return numCourses == 0
