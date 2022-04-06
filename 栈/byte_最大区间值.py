# 给定一个数组序列, 需要求选出一个区间, 使得该区间是所有区间中经过如下计算的值最大的一个：
#
# 区间中的最小数 * 区间所有数的和最后程序输出经过计算后的最大值即可，不需要输出具体的区间。如给定序列[6
# 2
# 1]则根据上述公式, 可得到所有可以选定各个区间的计算值:
#
# [6] = 6 * 6 = 36;
#
# [2] = 2 * 2 = 4;
#
# [1] = 1 * 1 = 1;
#
# [6, 2] = 2 * 8 = 16;
#
# [2, 1] = 1 * 3 = 3;
#
# [6, 2, 1] = 1 * 9 = 9;
#
# 从上述计算可见选定区间[6] ，计算值为
# 36， 则程序输出为
# 36。
#
# 区间内的所有数字都在[0, 100]
# 的范围内;

# 只用算每个nums[i]最长区间之和的乘积
# 记录nums[i]的最小左右区间
# 使用前缀和算总数
def pick_max(nums):
    n = len(nums)
    l, r = [0] * (n), [0] * (n)
    # 增加哨兵
    # nums = [0]+nums+[0]
    stack = []
    # 记录左边
    for i, num in enumerate(nums):
        while stack and stack[-1][0] >= num:
            stack.pop()
        l[i] = -1 if not stack else stack[-1][1]
        stack.append((num, i))
    stack.clear()
    # 记录右边
    for i, num in enumerate(reversed(nums)):
        while stack and stack[-1][0] >= num:
            stack.pop()
        r[n - 1 - i] = n if not stack else stack[-1][1]
        stack.append((num, n - 1 - i))
    # print(l,r)
    pre_sum = [0]
    # 计算前缀和
    for num in nums:
        pre_sum.append(pre_sum[-1] + num)
    pre_sum.pop(0)
    max_num = 0
    # 得到左边右边和前缀和，可以计算这个点最小的区间*nums[i]的值
    for i in range(n):
        left, right = l[i], r[i]
        tmp = pre_sum[right - 1] - (pre_sum[left] if left != -1 else 0)
        max_num = max(nums[i] * tmp, max_num)
    print(max_num)


n = int(input())
nums = list(map(int, input().split()))
pick_max(nums)
