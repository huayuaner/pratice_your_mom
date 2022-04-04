# 薯队长写了n篇笔记，编号从1~n,每篇笔记都获得了不少点赞数。
# 薯队长想从中选出一些笔记，作一个精选集合。挑选的时候有两个规则：
#  1.不能出现连续编号的笔记。
# 2.总点赞总数最多
# 如果满足1，2条件有多种方案，挑选笔记总数最少的那种
#
# 输入描述:
# 输入包含两行。第一行整数n表示多少篇笔记。 第二行n个整数分别表示n篇笔记的获得的点赞数。
#  （0<n<=1000,    0<=点赞数<=1000)
#
# 输出描述:
# 输出两个整数x,y。空格分割。
#  x表示总点赞数，y表示挑选的笔记总数。
#
# 输入例子1:
# 4
# 1 2 3 1
#
# 输出例子1:
# 4 2

n = int(input())
nums = list(map(int, input().split()))
def func(nums):
    dp = [0] * n
    cnt = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0],nums[1])
    cnt[0], cnt[1] = 1, 1
    for i in range(2, n):
        if dp[i-2] + nums[i] > dp[i-1]:
            dp[i] = dp[i-2] + nums[i]
            cnt[i] = cnt[i-2] + 1
        else:
            dp[i] = dp[i-1]
            cnt[i] = cnt[i-1]
    return dp[-1],cnt[-1]
if n<=2:
    print(max(nums))
else:
    ans = func(nums)
    print(ans[0], ans[1])