给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。

# 由于答案可能很大，因此 返回答案模 10^9 + 7 。
#
#  
#
# 示例 1：
#
# 输入：arr = [3,1,2,4]
# 输出：17
# 解释：
# 子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
# 最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
# 示例 2：
#
# 输入：arr = [11,81,94,43,3]
# 输出：444

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # sum_ = 0
        # n = len(arr)
        # for i in range(n):
        #     for j in range(i+1, n+1):
        #         sum_ = (sum_+min(arr[i:j])) % (pow(10,9)+7)
        #         #print(arr[i:j])
        # return sum_
        left, right = [], []
        stack = []
        n = len(arr)
        #得到左边界
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left.append(stack[-1] if stack else -1)
            stack.append(i)
        # print(left)
        stack.clear()
        #得到右边界
        for i in range(n - 1, -1, -1):
            #>=避免了arr中出现相同元素导致的重复计算
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right.append(stack[-1] if stack else n)
            stack.append(i)
        # print(right)
        ans = 0
        #映射范围的字串数*该元素等于元素的贡献值
        for i in range(n):
            ans = (ans + (arr[i] * (i - left[i]) * (right[n - i - 1] - i))) % (pow(10, 9) + 7)
        return ans



