# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#
# 注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。
#
#  
#
# 示例 1:
#
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 示例 2:
#
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        m,n = len(num1), len(num2)
        ans = [0]*(m+n)
        # 竖式乘法累加
        for i in range(m-1,-1,-1):
            x = int(num1[i])
            for j in range(n-1, -1, -1):
                ans[i+j+1] += x * int(num2[j])
        # print(ans)
        # 完成进位
        for i in range(m+n-1, 0,-1):
        # for i in range(1, m+n):
            ans[i-1] += ans[i] // 10
            ans[i] %= 10
        # print(ans)
        return ''.join(map(str, ans)).lstrip('0')
