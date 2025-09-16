# 给定一个大小为n的数组nums ，返回其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n / 2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#
#
# 示例
# 1：
#
# 输入：nums = [3, 2, 3]
# 输出：3
# 示例
# 2：
#
# 输入：nums = [2, 2, 1, 1, 1, 2, 2]
# 输出：2


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        candidate = 0
        for num in nums:
            if cnt == 0:
                candidate = num
                cnt += 1
            else:
                if num == candidate:
                    cnt += 1
                else:
                    cnt -= 1

        return candidate