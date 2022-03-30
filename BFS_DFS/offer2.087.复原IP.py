# 给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。
#
# 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
#
# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
#
#  
#
# 示例 1：
#
# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
# 示例 2：
#
# 输入：s = "0000"
# 输出：["0.0.0.0"]
# 示例 3：
#
# 输入：s = "1111"
# 输出：["1.1.1.1"]
# 示例 4：
#
# 输入：s = "010010"
# 输出：["0.10.0.10","0.100.1.0"]
# 示例 5：
#
# 输入：s = "10203040"
# 输出：["10.20.30.40","102.0.30.40","10.203.0.40"]
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # dfs
        # 搜寻可以到达的位置
        n = len(s)
        ans = []

        def dfs(pos, lis):
            if pos == n and len(lis) == 4:
                # print(lis,pos)
                nonlocal ans
                ans.append('.'.join(lis))
            if len(lis) >= 4 or pos >= n:
                return
            if s[pos] == '0':
                dfs(pos + 1, lis + [s[pos]])
            else:

                # for i in range(1,4):
                dfs(pos + 1, lis + [s[pos]])
                dfs(pos + 2, lis + [s[pos:pos + 2]])
                if 0 <= int(s[pos:pos + 3]) <= 255:
                    dfs(pos + 3, lis + [s[pos:pos + 3]])

        dfs(0, [])
        return ans
