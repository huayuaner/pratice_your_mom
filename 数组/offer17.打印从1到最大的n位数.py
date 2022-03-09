# 输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
#
# 示例 1:
#
# 输入: n = 1
# 输出: [1,2,3,4,5,6,7,8,9]
#  

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        # ans = []
        # for i in range(10**n):
        #     ans.append(i)
        # ans.pop(0)
        # return ans

        # 真正考核的是大数越界问题
        # 也就是遇到很大的数应该以字符串形式给到
        # 这样的dfs会带来两个两个问题：1.前缀0未删除 2.列表从0开始
        # 答主给出了使用两个变量确定开头位置，从而达到删除前缀0，并且增加判断删除0
        # 但是可以应用内置函数.lstrip('0')来删除前缀0
        def dfs(x):
            if x==n:
                s = ''.join(num)
                s = s.lstrip('0')
                if s!='':
                # 这里不能用int，因为大数越界
                    ans.append(int(s))
            else:
                for i in range(10):
                    num[x] = str(i)
                    dfs(x+1)
        num = ['0']*n
        ans = []
        dfs(0)
        return ans
