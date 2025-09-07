# 请你设计并实现一个满足
# LRU(最近最少使用)
# 缓存
# 约束的数据结构。
# 实现
# LRUCache
# 类：
# LRUCache(int
# capacity) 以
# 正整数
# 作为容量
# capacity
# 初始化
# LRU
# 缓存
# int
# get(int
# key) 如果关键字
# key
# 存在于缓存中，则返回关键字的值，否则返回 - 1 。
# void
# put(int
# key, int
# value) 如果关键字
# key
# 已经存在，则变更其数据值
# value ；如果不存在，则向缓存中插入该组
# key - value 。如果插入操作导致关键字数量超过
# capacity ，则应该
# 逐出
# 最久未使用的关键字。
# 函数
# get
# 和
# put
# 必须以
# O(1)
# 的平均时间复杂度运行。
#
#
#
# 示例：
#
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# 解释
# LRUCache
# lRUCache = new
# LRUCache(2);
# lRUCache.put(1, 1); // 缓存是
# {1 = 1}
# lRUCache.put(2, 2); // 缓存是
# {1 = 1, 2 = 2}
# lRUCache.get(1); // 返回
# 1
# lRUCache.put(3, 3); // 该操作会使得关键字
# 2
# 作废，缓存是
# {1 = 1, 3 = 3}
# lRUCache.get(2); // 返回 - 1(未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字
# 1
# 作废，缓存是
# {4 = 4, 3 = 3}
# lRUCache.get(1); // 返回 - 1(未找到)
# lRUCache.get(3); // 返回
# 3
# lRUCache.get(4); // 返回
# 4


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.size = 0

        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    # 添加到头部
    def _add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    # 删除节点
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # 移动到头部（表示最近访问）
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_to_head(node)

    # 移除尾部节点
    def _pop_tail(self):
        node = self.tail.prev
        self._remove_node(node)
        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if not node:
            node = DLinkedNode(key, value)
            self._add_to_head(node)
            self.cache[key] = node
            self.size += 1
            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)