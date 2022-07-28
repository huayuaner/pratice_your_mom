# 给定一个长度为 n 的整数数组 nums ，其中 nums 是范围为 [1，n] 的整数的排列。还提供了一个 2D 整数数组 sequences ，其中 sequences[i] 是 nums 的子序列。
# 检查 nums 是否是唯一的最短 超序列 。最短 超序列 是 长度最短 的序列，并且所有序列 sequences[i] 都是它的子序列。对于给定的数组 sequences ，可能存在多个有效的 超序列 。
#
# 例如，对于 sequences = [[1,2],[1,3]] ，有两个最短的 超序列 ，[1,2,3] 和 [1,3,2] 。
# 而对于 sequences = [[1,2],[1,3],[1,2,3]] ，唯一可能的最短 超序列 是 [1,2,3] 。[1,2,3,4] 是可能的超序列，但不是最短的。
# 如果 nums 是序列的唯一最短 超序列 ，则返回 true ，否则返回 false 。
# 子序列 是一个可以通过从另一个序列中删除一些元素或不删除任何元素，而不改变其余元素的顺序的序列。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,2,3], sequences = [[1,2],[1,3]]
# 输出：false
# 解释：有两种可能的超序列：[1,2,3]和[1,3,2]。
# 序列 [1,2] 是[1,2,3]和[1,3,2]的子序列。
# 序列 [1,3] 是[1,2,3]和[1,3,2]的子序列。
# 因为 nums 不是唯一最短的超序列，所以返回false。
# 示例 2：
#
# 输入：nums = [1,2,3], sequences = [[1,2]]
# 输出：false
# 解释：最短可能的超序列为 [1,2]。
# 序列 [1,2] 是它的子序列：[1,2]。
# 因为 nums 不是最短的超序列，所以返回false。

from collections import defaultdict
from collections import deque
import itertools
class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        # 只需要判断每两个相邻位置都存在即可
        # dic_pos = defaultdict(set)
        # for seq in sequences:
        #     for i in range(len(seq)-1):
        #         dic_pos[seq[i]].add(seq[i+1])
        # for i in range(len(nums)-1):
        #     if nums[i] not in dic_pos or nums[i+1] not in dic_pos[nums[i]]:
        #         return False
        # return True

        n = len(nums)
        # 拓扑图
        grid = [[] for _ in range(n)]
        # 计算每个节点的入度
        inDeg = [0] * n
        for seq in sequences:
            for pre, pos in itertools.pairwise(seq):
                grid[pre-1].append(pos-1)
                inDeg[pos-1] += 1
        pq = deque([i for i,d in enumerate(inDeg) if d == 0])
        while pq:
            if len(pq)>1:
                return False
            x = pq.popleft()
            for y in grid[x]:
                inDeg[y] -= 1
                if inDeg[y] == 0:
                    pq.append(y)
        return True