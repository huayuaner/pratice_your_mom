# 行程编码（Run-length encoding）是一种压缩算法，能让一个含有许多段连续重复数字的整数类型数组 nums 以一个（通常更小的）二维数组 encoded 表示。每个 encoded[i] = [vali, freqi] 表示 nums 中第 i 段重复数字，其中 vali 是该段重复数字，重复了 freqi 次。
#
# 例如， nums = [1,1,1,2,2,2,2,2] 可表示称行程编码数组 encoded = [[1,3],[2,5]] 。对此数组的另一种读法是“三个 1 ，后面有五个 2 ”。
# 两个行程编码数组 encoded1 和 encoded2 的积可以按下列步骤计算：
#
# 将 encoded1 和 encoded2 分别扩展成完整数组 nums1 和 nums2 。
# 创建一个新的数组 prodNums ，长度为 nums1.length 并设 prodNums[i] = nums1[i] * nums2[i] 。
# 将 prodNums 压缩成一个行程编码数组并返回之。
# 给定两个行程编码数组 encoded1 和 encoded2 ，分别表示完整数组 nums1 和 nums2 。nums1 和 nums2 的长度相同。 每一个 encoded1[i] = [vali, freqi] 表示 nums1 中的第 i 段，每一个 encoded2[j] = [valj, freqj] 表示 nums2 中的第 j 段。
#
# 返回 encoded1 和 encoded2 的乘积。
#
# 注：行程编码数组需压缩成可能的最小长度。
class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        # 指向code1和2中的二维数组
        # n = 0
        # for v,f in encoded1:
        #     n += f
        # i,j = 0,0
        # toti, totj = encoded1[0][1], encoded2[0][1]
        # index = 1
        # ans = []
        # pre = encoded1[i][0] * encoded2[j][0]
        # cnt = 1
        # while index<n:
        #     index += 1
        #     if index > toti:
        #         i += 1
        #         toti += encoded1[i][1]
        #     if index>totj:
        #         j += 1
        #         totj += encoded2[j][1]
        #     cur_val = encoded1[i][0] * encoded2[j][0]
        #     # print(cur_val,index)
        #     if pre == None or pre == cur_val:
        #         pre = cur_val
        #         cnt +=  + 1

        #     else:
        #         ans.append([pre, cnt])
        #         pre = cur_val
        #         cnt = 1
        #     if index == n:
        #             ans.append([pre, cnt])

        # return ans
        m, n = len(encoded1), len(encoded2)

        i = j = 0
        ans = [[-1, 0]]
        while i < m:
            # 记录数量
            # 两者中的较小值
            cnt = min(encoded1[i][1], encoded2[j][1])
            cur_val = encoded1[i][0] * encoded2[j][0]
            if cur_val == ans[-1][0]:
                ans[-1][1] += cnt
            else:
                ans.append([cur_val, cnt])
            encoded1[i][1] -= cnt
            if encoded1[i][1] == 0:
                i += 1
            encoded2[j][1] -= cnt
            if encoded2[j][1] == 0:
                j += 1
            # print(encoded1[i],encoded2[j])
        return ans[1:]



