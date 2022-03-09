# 给你一个整数数组 arr ，请使用 煎饼翻转 完成对数组的排序。
#
# 一次煎饼翻转的执行过程如下：
#
# 选择一个整数 k ，1 <= k <= arr.length
# 反转子数组 arr[0...k-1]（下标从 0 开始）
# 例如，arr = [3,2,1,4] ，选择 k = 3 进行一次煎饼翻转，反转子数组 [3,2,1] ，得到 arr = [1,2,3,4] 。
#
# 以数组形式返回能使 arr 有序的煎饼翻转操作所对应的 k 值序列。任何将数组排序且翻转次数在 10 * arr.length 范围内的有效答案都将被判断为正确。
# 示例 1：
#
# 输入：[3,2,4,1]
# 输出：[4,2,4,3]
# 解释：
# 我们执行 4 次煎饼翻转，k 值分别为 4，2，4，和 3。
# 初始状态 arr = [3, 2, 4, 1]
# 第一次翻转后（k = 4）：arr = [1, 4, 2, 3]
# 第二次翻转后（k = 2）：arr = [4, 1, 2, 3]
# 第三次翻转后（k = 4）：arr = [3, 2, 1, 4]
# 第四次翻转后（k = 3）：arr = [1, 2, 3, 4]，此时已完成排序。
# 示例 2：
#
# 输入：[1,2,3]
# 输出：[]
# 解释：
# 输入已经排序，因此不需要翻转任何内容。
# 请注意，其他可能的答案，如 [3，3] ，也将被判断为正确。
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # 每次排好最后一位
        ans = []

        for i in range(len(arr),0,-1):
            idx = arr.index(max(arr[:i]))
            # 说明该数字已经排好了
            if idx == i-1:
                continue
            # 使用两次反转将其放在正确位置
            # 1.将arr[:idx+1]反转，使得下标idx的数字在列表头
            # 2.将arr[:i]反转，使下标idx位置在i-1位置
            # for j in range((idx+1)//2):
            #     arr[j], arr[idx-j] = arr[idx-j], arr[j]
            # for j in range(i//2):
            #     arr[j], arr[i-1-j] = arr[i-1-j], arr[j]
            arr[:idx+1] = arr[idx::-1]
            arr[:i] = arr[i-1::-1]
            ans.append(idx+1)
            ans.append(i)
        #print(arr)
        return ans



