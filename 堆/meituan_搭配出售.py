# 服装店新进了a条领带，b条裤子，c个帽子，d件衬衫，现在要把这些搭配起来售卖。
# 有三种搭配方式，一条领带和一件衬衫，一条裤子和一件衬衫，一个帽子和一件衬衫。
# 卖出一套领带加衬衫可以得到e元，卖出一套裤子加衬衫可以得到f元，卖出一套帽子加衬衫可以得到g元。
# 现在你需要输出最大的获利方式



# 使用大根堆存  价格 数量  元组，每次弹出价格最高的那个品类
import heapq
a,b,c,d,e,f,g = map(int, input().split())
hq = []
heapq.heappush(hq, (-e,a))
heapq.heappush(hq,(-f,b))
heapq.heappush(hq, (-g,c))
ans = 0
while hq and d:
    p,n = heapq.heappop(hq)
    p = -p
    if n>d:
        ans += d*p
        d = 0
    else:
        ans += n*p
        d -= n
print(ans)