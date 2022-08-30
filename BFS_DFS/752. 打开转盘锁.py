# 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
#
# 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
#
# 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
#
# 字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。
#
#  
#
# 示例 1:
#
# 输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# 输出：6
# 解释：
# 可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
# 注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
# 因为当拨动到 "0102" 时这个锁就会被锁定。
# 示例 2:
#
# 输入: deadends = ["8888"], target = "0009"
# 输出：1
# 解释：把最后一位反向旋转一次即可 "0000" -> "0009"。
# 示例 3:
#
# 输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
# 输出：-1
# 解释：无法旋转到目标数字且不被锁定。
from collections import deque


# class Astar:
#     def __init__(self,state:str, target:str, g:int)->None:
#         self.state = state
#         # 当前步数
#         self.g = g
#         # 当前位置和目标位置的曼哈顿距离
#         self.h = Astar.getH(state, target)
#         self.f = self.g + self.h
#     @staticmethod
#     def getH(state:str, target:str):
#         res = 0
#         for i in range(4):
#             dis = abs(int(target[i]) - int(state[i]))
#             res += min(dis, 10-dis)
#         return res
#     def __lt__(self,other:'Astar')->bool:
#         return self.f < other.f

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # deadends = set(deadends)
        # if '0000' in deadends:
        #     return -1
        # pq = deque([('0000',0)])
        # seen = set(['0000'])
        # while pq:
        #     state, step = pq.popleft()
        #     if state == target:
        #         return step
        #     state = list(state)
        #     for i in range(4):
        #         tmp = state[i]
        #         state[i] = chr(ord(tmp) + 1) if tmp<'9' else '0'
        #         if (nex_state := ''.join(state)) not in seen and nex_state not in deadends:
        #             seen.add(nex_state)
        #             pq.append((nex_state,step+1))
        #         state[i] = chr(ord(tmp) - 1) if tmp>'0' else '9'
        #         if (nex_state := ''.join(state)) not in seen and nex_state not in deadends:
        #             seen.add(nex_state)
        #             pq.append((nex_state,step+1))
        #         state[i] = tmp
        #     # print(pq)
        # return -1

        # 双向bfs
        # 特判
        # deadends = set(deadends)
        # if '0000' in deadends:
        #     return -1
        # if target == '0000':
        #     return 0
        # def get(status: str) -> Generator[str, None, None]:
        #     s = list(status)
        #     for i in range(4):
        #         num = s[i]
        #         s[i] =  chr(ord(num) - 1) if num>'0' else '9'# num_prev(num)
        #         yield "".join(s)
        #         s[i] = chr(ord(num) + 1) if num<'9' else '0'# num_succ(num)
        #         yield "".join(s)
        #         s[i] = num
        # seen_front,seen_back = dict(),dict()
        # pq_f,pq_b = deque([('0000',0)]),deque([(target,0)])
        # seen_front['0000'] = 0
        # seen_back[target] = 0
        # while pq_f and pq_b:
        #     if len(pq_f) <= len(pq_b):
        #         cur_pq = pq_f
        #         seen = seen_front
        #         ohter_pq = pq_b
        #         other_seen = seen_back
        #     else:
        #         cur_pq = pq_b
        #         seen = seen_back
        #         ohter_pq = pq_f
        #         other_seen = seen_front
        #     for _ in range(len(cur_pq)):
        #         state,step = cur_pq.popleft()
        #         # print(step)
        #         for nex_state in get(state):
        #             if nex_state not in seen and nex_state not in deadends:
        #                 if nex_state in other_seen:
        #                     return step + 1 + other_seen[nex_state]
        #                 seen[nex_state] = step + 1
        #                 cur_pq.append((nex_state,step + 1))
        #         # print(pq_f,pq_b)
        # return -1

        # Astar
        if target == "0000":
            return 0

        dead = set(deadends)
        if "0000" in dead:
            return -1

        def num_prev(x: str) -> str:
            return "9" if x == "0" else str(int(x) - 1)

        def num_succ(x: str) -> str:
            return "0" if x == "9" else str(int(x) + 1)

        def get(status: str) -> Generator[str, None, None]:
            s = list(status)
            for i in range(4):
                num = s[i]
                s[i] = num_prev(num)
                yield "".join(s)
                s[i] = num_succ(num)
                yield "".join(s)
                s[i] = num

        def get_dis(state):
            res = 0
            for i in range(4):
                dis = abs(int(target[i]) - int(state[i]))
                res += min(dis, 10 - dis)
            return res

        pq = [(get_dis('0000'), '0000', 0)]
        seen = {'0000'}
        while pq:
            dis, state, step = heappop(pq)
            for nex in get(state):
                if nex not in seen and nex not in dead:
                    if nex == target:
                        return step + 1
                    seen.add(nex)
                    heappush(pq, (step + 1 + get_dis(nex), nex, step + 1))
        return -1





