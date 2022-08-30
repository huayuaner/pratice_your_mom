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
class helper:
    @staticmethod
    def quickSelect(arr, l , r, index):
        idx = helper.randomPartition(arr,l,r)
        if idx == index:
            # print(arr)
            return [arr[i][0] for i in range(idx,len(arr))]
        if idx < index:
            return helper.quickSelect(arr, idx+1, r, index)
        return helper.quickSelect(arr, l, idx-1, index)
    @staticmethod
    def randomPartition(arr, l, r):
        i = randint(l,r)
        # print(i,r,arr)
        arr[i],arr[r] = arr[r], arr[i]
        return helper.Partition(arr, l, r)
    def Partition(arr,l,r):
        base = arr[r]
        pivot = base[1]
        while l<r:
            while l<r and arr[l][1] < pivot:
                l += 1
            arr[l],arr[r] = arr[r], arr[l]
            while l<r and arr[r][1] >= pivot:
                r -= 1
            arr[l],arr[r] = arr[r], arr[l]
        arr[l] = base
        # print(arr)
        return l

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = list(Counter(nums).items())

        return helper.quickSelect(arr, 0, len(arr)-1, len(arr)-k)
        # cnts = Counter(nums)
        # hp = []
        # for key,val in cnts.items():
        #     if len(hp)<k:
        #         heappush(hp, (val, key))
        #     elif val > hp[0][0]:
        #         heappop(hp)
        #         heappush(hp, (val,key))
        #     # print(hp)
        # return [hp[i][1] for i in range(k)]

        # 快排
