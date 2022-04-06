#小强想要从[1,A]中选出一个整数x,从[1,B]中选出一个整数y .使得满足x/y=a/b 的同时且x和y的乘积最大。如果不存在这样的x和y,请输出“ 0 0”.


def gcd(x,y):
    m, n = (x, y) if x>=y else (y,x)
    while n:
        tmp = m%n
        m = n
        n = tmp
    return m
A, B, a, b = list(map(int, input().split()))
# 取a和b的最大公约数
m = gcd(a,b)
# print(m)
# 将a,b 化成最简
a = a//m
b = b//m
# 因为x/y = a/b所以有x/a = y/b
# t从A,B范围中的最大倍数中选择较小的满足两个区间情况
t = min(A//a, B//b)
# x,y有a,b得到
print(t*a, t*b)

# 要求x和y的乘积最大其实就是要x尽可能大（或y尽可能大），因为比例a/b已经固定了，y=x*b/a并没有什么操作空间。
# 先求取a和b的最大公约数将a/b化为最简分式，我们可以认为存在一个单元unit，使得x=a*unit，y=b*unit，因此可以得到unit1=x/a，unit2=y/b。
# 由x/y=a/b可知x/a=y/b，而x/a<=A/a，因此unit1<=A/a，同理unit2<=B/b，因此unit只需要同时满足不大于A/a和不大于B/b即可。又因为x要尽可能大，所以unit就要尽可能大，于是得到unit=min(A/a,B/b)
