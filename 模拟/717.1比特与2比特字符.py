有两种特殊字符：

第一种字符可以用一个比特 0 来表示
第二种字符可以用两个比特(10 或 11)来表示、
给定一个以 0 结尾的二进制数组 bits ，如果最后一个字符必须是一位字符，则返回 true 。

示例 1:

输入: bits = [1, 0, 0]
输出: true
解释: 唯一的编码方式是一个两比特字符和一个一比特字符。
所以最后一个字符是一比特字符。
示例 2:

输入: bits = [1, 1, 1, 0]
输出: false
解释: 唯一的编码方式是两比特字符和两比特字符。
所以最后一个字符不是一比特字符。

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # 动态规划
        # dp[i]表示前i个字符是否能被表示
        # dp = [False] * (len(bits)+1)
        # dp[0] = True
        # for i in range(1,len(dp)):
        #     if bits[i-1] != 1 or dp[i-1]!=True :
        #         dp[i] = True
        # #print(dp)
        # return dp[-2] #and bits[-1] == 0

        # 模拟
        n, i = len(bits), 0
        while i < n-1:
            # 遇到0走一步，遇到1走两步
            i += bits[i] + 1
        return i==n-1                
