line1 = input().split()
line1 = [int(x) for x in line1]
n, m = line1[0], line1[1]
line2 = input().split()
nums = [int(x) for x in line2]
line3 = input().split()
requirements = [int(x) for x in line3]

# print(n, m)
# print(nums)
# print(requirements)

# 滑动窗口
minLen = float("inf")
res = -1
l, r = 0, 0
window = dict()
requiredCnt = 0
satisfied = dict()

for i in range(1, m + 1):
    satisfied[i] = False


def checkSatisfied(nums):
    for value in nums.values():
        if not value:
            return False

    return True


for r in range(n):
    num = nums[r]

    if num not in window:
        window[num] = 1
    else:
        window[num] += 1

    if not satisfied[num] and requirements[num - 1] <= window[num]:
        requiredCnt += 1
        satisfied[num] = True
        # print("requiredCnt: ", requiredCnt, "l: ", l, "r: ", r)

    while requiredCnt == m and checkSatisfied(satisfied):
        if r - l + 1 < minLen:
            # print("更新：", l, r)
            minLen = r - l + 1

        numToRemove = nums[l]
        window[numToRemove] -= 1

        if satisfied[numToRemove] and window[numToRemove] < requirements[numToRemove - 1]:
            requiredCnt -= 1
            satisfied[numToRemove] = False

        l += 1

if minLen != float("inf"):
    print(minLen)
else:
    print(res)