# 小Q今天在上厕所时想到了这个问题：有n个数，两两组成二元组，相差最小的有多少对呢？相差最大呢？
from collections import Counter

while 1:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        nums.sort()
        cnt = Counter(nums)
        # 最大 最小的个数*最大的个数
        # 应该还有一种特殊的是最小等于最大
        # 那么就应该右n*(n-1)//2种
        max_cnt = cnt[nums[0]] * cnt[nums[-1]]
        min_cnt = 0
        repeat_num = [k for k in cnt.keys() if cnt[k] > 1]
        # 如果有重复值，最小差值一定为0
        if repeat_num:
            for n in repeat_num:
                count = cnt[n]
                min_cnt += count * (count - 1) // 2
        else:
            # 没有重复值
            min_gap = float("inf")
            for i in range(1, n):
                gap = nums[i] - nums[i - 1]
                if gap < min_gap:
                    min_gap = gap
                    min_cnt = 1
                elif gap == min_gap:
                    min_cnt += 1
        print(min_cnt, max_cnt)
    except:
        break
