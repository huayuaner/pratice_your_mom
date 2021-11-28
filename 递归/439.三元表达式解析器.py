给定一个以字符串表示的任意嵌套的三元表达式，计算表达式的值。你可以假定给定的表达式始终都是有效的并且只包含数字 0-9, ?, :, T 和 F (T 和 F 分别表示真和假）。

# 注意：
#
# 给定的字符串长度 ≤ 10000。
# 所包含的数字都只有一位数。
# 条件表达式从右至左结合（和大多数程序设计语言类似）。
# 条件是 T 和 F其一，即条件永远不会是数字。
# 表达式的结果是数字 0-9, T 或者 F。

# 输入： "T?2:3"
#
# 输出： "2"
#
# 解释： 如果条件为真，结果为 2；否则，结果为 3。

def parseTernary(self, expression: str) -> str:
    print(pos)
    if expression.find('?')== -1:
        return expression
    s = expression[0]
    pos = 2
    count = 1
    while pos < len(expression):
        if expression[pos] == '?':
            count +=1
        elif expression[pos] == ':':
            count -= 1
        if count == 0:
            break
        pos += 1

    if s == 'T':

        return self.parseTernary(expression[2: pos])
    else:
        return self.parseTernary(expression[pos+1:])
