# n 张多米诺骨牌排成一行，将每张多米诺骨牌垂直竖立。在开始时，同时把一些多米诺骨牌向左或向右推。
#
# 每过一秒，倒向左边的多米诺骨牌会推动其左侧相邻的多米诺骨牌。同样地，倒向右边的多米诺骨牌也会推动竖立在其右侧的相邻多米诺骨牌。

# 如果一张垂直竖立的多米诺骨牌的两侧同时有多米诺骨牌倒下时，由于受力平衡， 该骨牌仍然保持不变。
#
# 就这个问题而言，我们会认为一张正在倒下的多米诺骨牌不会对其它正在倒下或已经倒下的多米诺骨牌施加额外的力。
#
# 给你一个字符串 dominoes 表示这一行多米诺骨牌的初始状态，其中：
#
# dominoes[i] = 'L'，表示第 i 张多米诺骨牌被推向左侧，
# dominoes[i] = 'R'，表示第 i 张多米诺骨牌被推向右侧，
# dominoes[i] = '.'，表示没有推动第 i 张多米诺骨牌。
# 返回表示最终状态的字符串。
#
#  
# 示例 1：
#
# 输入：dominoes = "RR.L"
# 输出："RR.L"
# 解释：第一张多米诺骨牌没有给第二张施加额外的力。

# 输入：dominoes = ".L.R...LR..L.."
# 输出："LL.RR.LLRRLL.."

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # BFS
        # 超时
        # 原因是它对于一个点在t时间点有推倒和再立起两个动作，有重复操作
        # 而下面那个bfs它是记录了t时间点该点所有的力，只受到一个力才推倒
        n = len(dominoes)
        dominoes = list(dominoes)
        # 记录点受力的时间点
        g = [0] * n
        pq = []
        for i, domino in enumerate(dominoes):
            if domino != '.':
                dir = -1 if domino == 'L' else 1
                # 每次记录3个信息，位置，时间点，方向
                pq.append((i, 1, dir))
                g[i] = 1
        while pq:
            pos, time, dir = pq.pop(0)
            nex_pos = pos + dir
            # 当超出时跳过
            if dominoes[pos] == '.' or nex_pos < 0 or nex_pos > n - 1: continue
            # 首次受力
            if g[nex_pos] == 0:
                pq.append((nex_pos, time + 1, dir))
                g[nex_pos] = time + 1
                # print(nex_pos)
                dominoes[nex_pos] = 'L' if dir == -1 else 'R'
            # 在当前这个时间点同时受到的两个力，保持平衡，不是统一时间点则以先的为准
            elif g[nex_pos] == time + 1:
                dominoes[nex_pos] = '.'
        return ''.join(dominoes)

        # 模拟 + 双指针
        # s = list(dominoes)
        # n, i, left = len(s), 0, 'L'
        # while i < n:
        #     # 左指针
        #     j = i
        #     # 找到一段都是'.'的位置
        #     while j < n and s[j] == '.':
        #         j += 1
        #     # 判断这段'.'的左右分别是什么
        #     right = s[j] if j<n else 'R'
        #     # 相同就直接变成一样
        #     if right == left:
        #         while i<j:
        #             s[i] = right
        #             i += 1
        #     # 不同就往中间倒
        #     elif left == 'R' and right =='L':
        #         k = j-1
        #         while i < k:
        #             s[i] = 'R'
        #             s[k] = 'L'
        #             i += 1
        #             k -= 1
        #     # 更新i
        #     # 更新left
        #     i = j + 1
        #     left = right
        # return ''.join(s)

        # n = len(dominoes)
        # q = deque()
        # time = [-1] * n
        # force = [[] for _ in range(n)]
        # for i, f in enumerate(dominoes):
        #     if f != '.':
        #         q.append(i)
        #         time[i] = 0
        #         force[i].append(f)

        # res = ['.'] * n
        # while q:
        #     i = q.popleft()
        #     if len(force[i]) == 1:
        #         res[i] = f = force[i][0]
        #         ni = i - 1 if f == 'L' else i + 1
        #         if 0 <= ni < n:
        #             t = time[i]
        #             if time[ni] == -1:
        #                 q.append(ni)
        #                 time[ni] = t + 1
        #                 force[ni].append(f)
        #             elif time[ni] == t + 1:
        #                 force[ni].append(f)
        # return ''.join(res)






