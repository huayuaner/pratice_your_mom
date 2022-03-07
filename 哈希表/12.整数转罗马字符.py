罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给你一个整数，将其转为罗马数字。

 

示例 1:

输入: num = 3
输出: "III"
示例 2:

输入: num = 4
输出: "IV"
示例 3:

输入: num = 9
输出: "IX"
示例 4:

输入: num = 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.
示例 5:

输入: num = 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.

class Solution:
    # 放入了所有对应的罗马字符
    VALUE_SYMBOLS = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    def intToRoman(self, num: int) -> str:
        roman = list()
        # 遍历列表
        for value, symbol in Solution.VALUE_SYMBOLS:
            # 当前num大于等于value时就往roman中放入相应的字符直到num小于该value
            while num >= value:
                num -= value
                roman.append(symbol)
            if num == 0:
                break
            # 将结果连接起来
        return "".join(roman)


    # def intToRoman(self, num: int) -> str:
    #     HashMap = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
    #     ans = ""
    #     div = 1000 
    #     while div:
    #         digit = num // div
    #         #print(digit,div)
    #         if digit <= 5:
    #             if digit >= 4:
    #                 ans += (5-digit)*HashMap[div] + HashMap[5*div]
    #             else:
    #                 ans += digit * HashMap[div]
    #         else:
    #             if digit == 9:
    #                 ans += HashMap[div] + HashMap[div*10]
    #             else:
    #                 ans += HashMap[5*div] + (digit-5)*HashMap[div]
            
    #         num = num%div
    #         div = div//10
    #     return ans