# 我们有 n 种不同的贴纸。每个贴纸上都有一个小写的英文单词。
#
# 您想要拼写出给定的字符串 target ，方法是从收集的贴纸中切割单个字母并重新排列它们。如果你愿意，你可以多次使用每个贴纸，每个贴纸的数量是无限的。
#
# 返回你需要拼出 target 的最小贴纸数量。如果任务不可能，则返回 -1 。
#
# 注意：在所有的测试用例中，所有的单词都是从 1000 个最常见的美国英语单词中随机选择的，并且 target 被选择为两个随机单词的连接。
#
#  
#
# 示例 1：
#
# 输入： stickers = ["with","example","science"], target = "thehat"
# 输出：3
# 解释：
# 我们可以使用 2 个 "with" 贴纸，和 1 个 "example" 贴纸。
# 把贴纸上的字母剪下来并重新排列后，就可以形成目标 “thehat“ 了。
# 此外，这是形成目标字符串所需的最小贴纸数量。
# 示例 2:
#
# 输入：stickers = ["notice","possible"], target = "basicbasic"
# 输出：-1
# 解释：我们不能通过剪切给定贴纸的字母来形成目标“basicbasic”。

from collections import Counter
from collections import deque


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        cnt_tar = [0] * 26
        for c in target:
            cnt_tar[ord(c) - ord('a')] += 1

        # target_set = set(target)
        def avaliable(s):

            cnt = Counter()
            for c in s:
                if c in target:
                    cnt[c] += 1
            return cnt

        sti = [c for st in stickers if (c := avaliable(st))]
        # print(sti)
        pq = deque()
        pq.append((cnt_tar, 0))
        seen = set()
        seen.add(tuple(cnt_tar))
        while pq:
            cnt, step = pq.popleft()
            if sum(cnt) == 0:
                return step
            for a in sti:
                # 注意list的复制
                tmp = cnt[:]
                for c in a:
                    if a[c] >= tmp[ord(c) - ord('a')]:
                        tmp[ord(c) - ord('a')] = 0
                    else:
                        tmp[ord(c) - ord('a')] -= a[c]
                # print(tmp, a, step)
                if tuple(tmp) not in seen:
                    seen.add(tuple(tmp))
                    pq.append((tmp, step + 1))
            # print(pq)
        return -1

        # m = len(target)
        # @functools.lru_cache(None)
        # def dp(mask: int) -> int:
        #     if mask == 0:
        #         return 0
        #     res = m + 1
        #     for sticker in stickers:
        #         left = mask
        #         cnt = Counter(sticker)
        #         for i, c in enumerate(target):
        #             if mask >> i & 1 and cnt[c]:
        #                 cnt[c] -= 1
        #                 left ^= 1 << i
        #         if left < mask:
        #             res = min(res, dp(left) + 1)
        #     return res
        # res = dp((1 << m) - 1)
        # return res if res <= m else -1













