# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#  
#
# 示例 1：
#
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
# 示例 2：
#
# 输入：n = 1
# 输出：["()"]
#  
#
# 提示：
#
# 1 <= n <= 8

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # dfs 回溯
        # left,right代表左右括号剩余的数量
        # def dfs(str_,left,right):
        #     if left == 0 and right == 0:
        #         self.ans.append(str_)
        #         return 
        #     # 左右相等只能用左括号
        #     if left == right:
        #         dfs(str_+"(", left-1, right)
        #     # 左括号的比右多，左右都可以
        #     if left < right:
        #         if left > 0:
        #             dfs(str_+"(", left-1, right)
                
        #         dfs(str_+")", left, right-1)
        # self.ans = []
        # dfs("", n, n)
        # return self.ans
        if n == 0:
            return []
        total_l = []
        total_l.append([None])    # 0组括号时记为None
        total_l.append(["()"])    # 1组括号只有一种情况
        for i in range(2,n+1):    # 开始计算i组括号时的括号组合
            l = []        
            for j in range(i):    # 将n-1情况分成两个部分，list1，list2，对应位置相加为n-1，代码中为i-1
                now_list1 = total_l[j]    
                now_list2 = total_l[i-1-j]    
                for k1 in now_list1:  
                    for k2 in now_list2:
                        if k1 == None:
                            k1 = ""
                        if k2 == None:
                            k2 = ""
                        el = "(" + k1 + ")" + k2 #新增的括号只能一部分在中间，一部分在右侧，由于遍历，左右对称为题解决
                        l.append(el)    # 把所有可能的情况添加到 l 中
            
            total_l.append(l)    # l这个list就是i组括号的所有情况，添加到total_l中，继续求解i=i+1的情况
            print(total_l)
        return total_l[n]

