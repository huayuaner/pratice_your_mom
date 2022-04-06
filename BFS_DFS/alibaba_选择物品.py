# 有n个物品可供选择，必须选择m其中个物品，请按字典序顺序输出所有选取方案的物品编号
#
# 123与312与321等被认为是同一种方案，输出字典序最小的123即可
# 接收输入
n, k = list(map(int, input().split()))


def dfs(pos, lis):
    if len(lis) == k:
        for num in lis:
            print(num, end=' ')
        print()
        return
    # if len(lis)>k:
    # return
    # dfs+回溯
    for i in range(pos + 1, n+1):
        lis.append(i)
        dfs(i, lis)
        lis.pop()

dfs(0, [])
