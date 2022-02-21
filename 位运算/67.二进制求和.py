给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

 

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"

# 位运算
        # 将a,b 换成10进制的结果
        # x, y = int(a, 2), int(b, 2)
        # #print(x,y)
        # # 当进位为0是结束
        # while y:
        #     # 计算所有位置应该相加后的结果
        #     answer = x ^ y
        #     # 同时计算所有位置的进位，由于进位往前一位，所以左移一位
        #     carry = (x & y) << 1
        #     x, y = answer, carry
        #     print(answer,carry)
        # # bin(x)让x以2进制字符串形式输出，但是会加上前缀"0b"，所以从第3个字符开始
        # return bin(x)[2:]
  x, y = int(a, 2), int(b, 2)
        #print(x,y)
        # 当进位为0是结束
        
            # 计算所有位置应该相加后的结果
        answer = x ^ y
        # 同时计算所有位置的进位，由于进位往前一位，所以左移一位
        carry = (x & y) << 1
        ans = answer+carry
        #print(answer,carry)
        # bin(x)让x以2进制字符串形式输出，但是会加上前缀"0b"，所以从第3个字符开始
        return bin(ans)[2:]
