# 基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 'A'、'C'、'G' 和 'T' 之一。
#
# 假设我们需要调查从基因序列 start 变为 end 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。
#
# 例如，"AACCGGTT" --> "AACCGGTA" 就是一次基因变化。
# 另有一个基因库 bank 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。
#
# 给你两个基因序列 start 和 end ，以及一个基因库 bank ，请你找出并返回能够使 start 变化为 end 所需的最少变化次数。如果无法完成此基因变化，返回 -1 。
#
# 注意：起始基因序列 start 默认是有效的，但是它并不一定会出现在基因库中。
#
#  
#
# 示例 1：
#
# 输入：start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
# 输出：1
# 示例 2：
#
# 输入：start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
# 输出：2
# 示例 3：
#
# 输入：start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
# 输出：3
from collections import deque


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0
        bank_set = set(bank)
        if end not in bank_set:
            return -1
        seen = [set(), set()]
        pq = [deque(), deque()]
        pq[0].append(start)
        seen[0].add(start)
        pq[1].append(end)
        seen[1].add(end)
        step = 0
        while pq[0] and pq[1]:
            # print(pq)
            idx = (1 if len(pq[1]) < len(pq[0]) else 0)
            oppo = (1 if idx == 0 else 0)

            for _ in range(len(pq[idx])):
                word = pq[idx].popleft()
                # print(word, seen[oppo])
                # 终止条件
                if word in seen[oppo]:
                    # print(word, seen[oppo], idx, oppo)
                    return step
                # 寻找所有变化
                for i in range(8):
                    for c in 'ACGT':
                        if word[i] == c:
                            continue
                        new_word = word[:i] + c + word[i + 1:]
                        # 满足条件的变化才会放进pq中
                        if new_word not in seen[idx] and new_word in bank_set:
                            seen[idx].add(new_word)
                            pq[idx].append(new_word)
            step += 1
            # s, step = pq.popleft()
            # if s == end:
            #     return step
            # for i in range(8):
            #     for c in ['A', 'C', 'G', 'T']:
            #         if s[i] == c:
            #             continue
            #         new_s = s[:i] + c + s[i+1:]
            #         if new_s in bank and new_s not in seen:
            #             seen.add(new_s)
            #             pq.append((new_s,step+1))
        return -1