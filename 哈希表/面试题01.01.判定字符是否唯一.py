实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

示例 1：

输入: s = "leetcode"
输出: false 
示例 2：

输入: s = "abc"
输出: true

        # 位运算
        mark = 0
        for char in astr:
            bit = ord(char) - ord('a')
            if mark & (1<<bit) != 0:
                return False
            else:
                mark |= (1<<bit)
        return True