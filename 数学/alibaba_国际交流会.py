# 最近小强主办了一场国际交流会，大家在会上以一个圆桌围坐在一起。
# 由于大会的目的就是让不同国家的人感受一下不同的异域气息，
# 为了更好地达到这个目的，小强希望最大化邻座两人之间的差异程度和。为此，他找到了你，希望你能给他安排一下座位，
# 达到邻座之间的差异之和最大。

# 要想相邻元素的绝对差之和最大，就要保证所有数对的绝对差尽可能均匀分布。进行如下操作就可以达到这个效果：
# 先将数组进行排序，然后将其分为前后两个子数组，按顺序取出两个子数组的元素组成数对。

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
ans = []
half = n//2
# 分成大小，其中一个逆序
big = nums[half:]
#
small = [nums[i] for i in range(half-1,-1, -1)]
i,j = 0, 0
# print(big,small)
while i<half and j < n-half:
    ans.append(big[j])
    ans.append(small[i])
    j+=1
    i+=1
if n%2==1:
    ans.append(big[-1])
total = 0
for i in range(n):
    if i == n-1:
        total += abs(ans[i]-ans[0])
    else:
        total += abs(ans[i]-ans[i+1])
print(total)
for n in ans:
    print(n, end=' ')