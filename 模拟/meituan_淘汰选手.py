# 某比赛已经进入了淘汰赛阶段,已知共有n名选手参与了此阶段比赛，他们的得分分别是a_1,a_2….a_n,小美作为比赛的裁判希望设定一个分数线m，使得所有分数大于m的选手晋级，其他人淘汰。
#
# 但是为了保护粉丝脆弱的心脏，小美希望晋级和淘汰的人数均在[x,y]之间。
#
# 显然这个m有可能是不存在的，也有可能存在多个m，如果不存在，请你输出-1，如果存在多个，请你输出符合条件的最低的分数线。


n, x, y = list(map(int, input().split())) # 获取n, x, y 的值，n代表人数，下x,y代表范围
score = list(map(int, input().split())) #进行排序
score.sort()
if 2 * y < n:
    print(-1)
else:
    # 确定淘汰人数
    left_length = 0
    for i in range(x, y + 1):
        if x <= n - i <= y:
            left_length = i
            break

    print(score[left_length - 1])