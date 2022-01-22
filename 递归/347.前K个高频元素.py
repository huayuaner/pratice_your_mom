# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
#
#  
#
# 示例 1:
#
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 示例 2:
#
# 输入: nums = [1], k = 1
# 输出: [1]
#
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # cnt = Counter(nums)
        # ans = sorted(cnt.items(),key = lambda x:x[1],reverse = True)
        # return [ans[i][0] for i in range(k)]

        # 堆方法
        cnt = Counter(nums)
        pq = []
        for i in cnt:
            # 堆长度小于k直接放入
            if len(pq) < k:
                heappush(pq, (cnt[i], i))
            # 等于k比较其中的最小出现频率，大于则替换
            else:
                if cnt[i] > pq[0][0]:
                    heappop(pq)
                    heappush(pq, (cnt[i], i))
        return [pq[i][1] for i in range(k)]
