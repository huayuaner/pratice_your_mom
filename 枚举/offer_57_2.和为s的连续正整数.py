输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # 暴力枚举
        # ans = []
        # start = 1
        # while start<target:
        #     end = start
        #     tmp = []
        #     sum_ = 0
        #     while end<target:
        #         sum_ += end
        #         tmp.append(end)
        #         if sum_ < target:
        #             end += 1
        #             if end == target:
        #                 start += 1
        #                 break
        #         elif sum_ == target:
        #             if end-start+1>1:
        #                 ans.append(tmp)
        #             start += 1
        #             break
        #         else:
        #             start += 1
        #             break
        #     #print(start,end,sum_,ans)
        # return ans

        # 滑动窗口
        L, R = 1, 1
        sum_ = 0
        ans = []
        # 左闭右开的滑动窗口
        while L <= target // 2:
            if sum_ < target:
                sum_ +=R
                R += 1 
            elif sum_ > target:
                sum_ -= L
                L += 1
            else:
                ans.append(list(range(L,R)))
                # 左边界向右移动
                sum_ -= L 
                L += 1
        return ans

                 