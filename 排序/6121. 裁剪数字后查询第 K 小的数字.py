from collections import deque


class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        # 增量排序
        qs = sorted(zip(queries, range(len(queries))), key=lambda x: x[0][1])
        a = sorted(zip(nums, range(len(nums))), key=lambda x: x[0][-1])  # 按照最后一个字符排序
        j = 2  # 当前排序到了倒数第几个字符（之前已经按最后一个字符排序了）
        ans = [0] * len(queries)
        for (k, trim), i in qs:
            while j <= trim:

                # a.sort(key = lambda x:x[0][-j]) # 每次只对倒数第j个字符进行排序（因为j之后的字符都排序了，所以只对第j个字符排序即完成了对包括j之后的所有字符排序，这里可以用桶排序）
                bucket = [[] for _ in range(10)]
                for num, idx in a:
                    bucket[int(num[-j])].append((num, idx))
                b_idx = 0
                for idx in range(len(a)):
                    while not bucket[b_idx]:
                        b_idx += 1
                    a[idx] = bucket[b_idx].popleft()

                j += 1
            # print(a,j,i,k)
            ans[i] = a[k - 1][1]
            # print(ans)
        return ans
