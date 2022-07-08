# 给你个整数数组 arr，其中每个元素都 不相同。
#
# 请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。
#
#  
#
# 示例 1：
#
# 输入：arr = [4,2,1,3]
# 输出：[[1,2],[2,3],[3,4]]
# 示例 2：
#
# 输入：arr = [1,3,6,10,15]
# 输出：[[1,3]]
# 示例 3：
#
# 输入：arr = [3,8,-10,23,19,-4,-14,27]
# 输出：[[-14,-10],[19,23],[23,27]]
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        min_gap = float('inf')
        for i in range(len(arr)-1):
            if (tmp:=arr[i+1] - arr[i]) == min_gap:
                # print(ans)
                ans.append([arr[i], arr[i+1]])
                # print(ans)
            elif tmp < min_gap:
                # ans.clear()
                # ans.append([arr[i], arr[i+1]])
                ans = [[arr[i], arr[i+1]]]
                min_gap = tmp
        return ans

