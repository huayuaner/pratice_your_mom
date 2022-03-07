# 给你一个整数数组 arr ，你一开始在数组的第一个元素处（下标为 0）。
#
# 每一步，你可以从下标 i 跳到下标：
#
# i + 1 满足：i + 1 < arr.length
# i - 1 满足：i - 1 >= 0
# j 满足：arr[i] == arr[j] 且 i != j
# 请你返回到达数组最后一个元素的下标处所需的 最少操作次数 。
#
# 注意：任何时候你都不能跳到数组外面。
#
#  
#
# 示例 1：
#
# 输入：arr = [100,-23,-23,404,100,23,23,23,3,404]
# 输出：3
# 解释：那你需要跳跃 3 次，下标依次为 0 --> 4 --> 3 --> 9 。下标 9 为数组的最后一个元素的下标。
# 示例 2：
#
# 输入：arr = [7]
# 输出：0
# 解释：一开始就在最后一个元素处，所以你不需要跳跃。
# 示例 3：
#
# 输入：arr = [7,6,9,6,9,6,9,7]
# 输出：1
# 解释：你可以直接从下标 0 处跳到下标 7 处，也就是数组的最后一个元素处。
# 示例 4：
#
# 输入：arr = [6,1,9]
# 输出：2
# 示例 5：
#
# 输入：arr = [11,22,7,7,7,7,7,7,7,22,13]
# 输出：3
#
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        #将每个值的位置存起来
        idxSameValue = dict()
        for i, num in enumerate(arr):
            if num not in idxSameValue:
                idxSameValue[num] = []
            idxSameValue[num].append(i)
        #保存访问过的idx
        visited = set()
        #广度有限的队列
        q = deque()
        #队列放入当前位置和走的步数
        q.append([0,0])
        #加入访问的初始点
        visited.add(0)
        # 广度优先搜索
        while q:
            idx, step = q.popleft()
            # 返回条件
            if idx == len(arr) -1 :
                return step
            # 得到这个点对应的值
            num = arr[idx]
            # 步数加一
            step += 1
            # 将它可以跳跃的所有点加入队列
            if num in idxSameValue:
                for i in idxSameValue[num]:
                    #print(1)
                    if i not in visited:
                        q.append([i, step])
                        visited.add(i)
                # 删除这个num对应的路径
                del idxSameValue[num]
            # 往前一步加入队列
            if idx+1 < len(arr) and idx+1 not in visited:
                q.append([idx+1, step])
                visited.add(idx+1)
            # 往后一步加入队列
            if idx-1 > -1  and idx-1 not in visited:
                q.append([idx-1, step])
                visited.add(idx-1)