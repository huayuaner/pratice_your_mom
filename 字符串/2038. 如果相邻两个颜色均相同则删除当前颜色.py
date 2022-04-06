# 总共有 n 个颜色片段排成一列，每个颜色片段要么是 'A' 要么是 'B' 。给你一个长度为 n 的字符串 colors ，其中 colors[i] 表示第 i 个颜色片段的颜色。
#
# Alice 和 Bob 在玩一个游戏，他们 轮流 从这个字符串中删除颜色。Alice 先手 。
#
# 如果一个颜色片段为 'A' 且 相邻两个颜色 都是颜色 'A' ，那么 Alice 可以删除该颜色片段。Alice 不可以 删除任何颜色 'B' 片段。
# 如果一个颜色片段为 'B' 且 相邻两个颜色 都是颜色 'B' ，那么 Bob 可以删除该颜色片段。Bob 不可以 删除任何颜色 'A' 片段。
# Alice 和 Bob 不能 从字符串两端删除颜色片段。
# 如果其中一人无法继续操作，则该玩家 输 掉游戏且另一玩家 获胜 。
# 假设 Alice 和 Bob 都采用最优策略，如果 Alice 获胜，请返回 true，否则 Bob 获胜，返回 false。
#
#  
#
# 示例 1：
#
# 输入：colors = "AAABABB"
# 输出：true
# 解释：
# AAABABB -> AABABB
# Alice 先操作。
# 她删除从左数第二个 'A' ，这也是唯一一个相邻颜色片段都是 'A' 的 'A' 。
#
# 现在轮到 Bob 操作。
# Bob 无法执行任何操作，因为没有相邻位置都是 'B' 的颜色片段 'B' 。
# 因此，Alice 获胜，返回 true 。
# 示例 2：
#
# 输入：colors = "AA"
# 输出：false
# 解释：
# Alice 先操作。
# 只有 2 个 'A' 且它们都在字符串的两端，所以她无法执行任何操作。
# 因此，Bob 获胜，返回 false 。
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # 计数
        # 两者之间的删除并不影响对方的操作
        # 记录两者能删的字母数量，比较大小即可
        cnt_A = 0
        cnt_B = 0
        lens = 1
        colors = colors+'C'
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                lens += 1
            else:
                if colors[i-1] == 'B':
                    if lens>=3:
                        cnt_B += lens-2
                else:
                    if lens>=3:
                        cnt_A += lens-2
                lens = 1
        # print(cnt_A, cnt_B)
        return True if cnt_A>cnt_B else False
