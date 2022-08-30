# 有 n 个人被分成数量未知的组。每个人都被标记为一个从 0 到 n - 1 的唯一ID 。
#
# 给定一个整数数组 groupSizes ，其中 groupSizes[i] 是第 i 个人所在的组的大小。例如，如果 groupSizes[1] = 3 ，则第 1 个人必须位于大小为 3 的组中。
#
# 返回一个组列表，使每个人 i 都在一个大小为 groupSizes[i] 的组中。
#
# 每个人应该 恰好只 出现在 一个组 中，并且每个人必须在一个组中。如果有多个答案，返回其中 任何 一个。可以 保证 给定输入 至少有一个 有效的解。
from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # 组的大小对应该组还能放几个人
        dic = defaultdict(list)
        ans = []
        for i, group in enumerate(groupSizes):
            dic[group].append(i)
            # if len(dic[group]) == group:
            # ans.append(dic[group])
            # del dic[group]
        for k, v in dic.items():
            for i in range(0, len(v), k):
                ans.append(v[i:i + k])

        return ans

        # dic = dict()
        # ans = []
        # for i, group in enumerate(groupSizes):
        #     if group not in dic or len(ans[dic[group]]) == group:
        #         dic[group] = len(ans)
        #         ans.append([i])
        #     else:
        #         ans[dic[group]].append(i)
        # return ans


