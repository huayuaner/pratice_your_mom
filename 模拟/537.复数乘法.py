# 复数 可以用字符串表示，遵循 "实部+虚部i" 的形式，并满足下述条件：
#
# 实部 是一个整数，取值范围是 [-100, 100]
# 虚部 也是一个整数，取值范围是 [-100, 100]
# i2 == -1
# 给你两个字符串表示的复数 num1 和 num2 ，请你遵循复数表示形式，返回表示它们乘积的字符串。
#
#  
#
# 示例 1：
#
# 输入：num1 = "1+1i", num2 = "1+1i"
# 输出："0+2i"
# 解释：(1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。
# 示例 2：
#
# 输入：num1 = "1+-1i", num2 = "1+-1i"
# 输出："0+-2i"
# 解释：(1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # idx_1 = num1.find('+')
        # idx_2 = num2.find('+')
        # shi = int(num1[:idx_1])*int(num2[:idx_2]) - int(num1[idx_1+1:-1]) * int(num2[idx_2+1:-1])
        # xu = int(num1[idx_1+1:-1])*int(num2[:idx_2]) + int(num1[:idx_1])*int(num2[idx_2+1:-1])
        # return str(shi)+ '+' +str(xu)+'i'
        real1, imag1 = map(int, num1[:-1].split('+'))
        real2, imag2 = map(int, num2[:-1].split('+'))
        return'{}+{}i'.format(real1*real2-imag1*imag2,real1*imag2+imag1*real2)