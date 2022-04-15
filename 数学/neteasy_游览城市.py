#
# 魔法王国一共有n个城市,编号为0~n-1号,n个城市之间的道路连接起来恰好构成一棵树。
# 小易现在在0号城市,每次行动小易会从当前所在的城市走到与其相邻的一个城市,小易最多能行动L次。
# 如果小易到达过某个城市就视为小易游历过这个城市了,小易现在要制定好的旅游计划使他能游历最多的城市,请你帮他计算一下他最多能游历过多少个城市(注意0号城市已经游历了,游历过的城市不重复计算)。


n,l = list(map(int, input().split()))
mapping = list(map(int, input().split()))
length = [0]*n
# 总共n-1条路
# 记录每条路的长度
for i in range(n-1):
    length[i+1] = length[mapping[i]] + 1
maxlen = max(length)
# 能移动的步数小于最大长度
if l<=maxlen:
    print(l+1)
else:
    # 超过最大长度就先用剩余的步数游览城市再返回原点，最后游览最长路径
    print(maxlen+1+(l-maxlen)//2)