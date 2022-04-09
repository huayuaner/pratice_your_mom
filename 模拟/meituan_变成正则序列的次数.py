# 我们称一个长度为n的序列为正则序列，当且仅当该序列是一个由1~n组成的排列，即该序列由n个正整数组成，取值在[1,n]范围，且不存在重复的数，同时正则序列不要求排序
#
# 有一天小团得到了一个长度为n的任意序列s，他需要在有限次操作内，将这个序列变成一个正则序列，每次操作他可以任选序列中的一个数字，并将该数字加一或者减一。
#
# 请问他最少用多少次操作可以把这个序列变成正则序列？


# 思路
# 排序后每个数字的位置变成对应位置正则数的次数是最小的
from sys import stdin

n = int(input())
nums = list(map(int, stdin.readline().split()))
nums.sort()
cnt = 0
for i, n in enumerate(nums):
    cnt += abs(i + 1 - n)
print(cnt)
