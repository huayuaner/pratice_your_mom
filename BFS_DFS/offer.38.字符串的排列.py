# 打印出该字符串中字符的所有排列打印出该字符串中字符的所有排列输入一个字符串，打印出该字符串中字符的所有排列。
#
#  
#
# 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
#
#  
#
# 示例:
#
# 输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]

class Solution:
    def permutation(self, s: str) -> List[str]:
        ans = []
        c = list(s)
        # 每次固定一个位置的字符
        def dfs(pos):
            # 当确定位置达到末尾，说明已经固定完成
            if pos == len(c) - 1:
                ans.append(''.join(c))
                return 
            # 去重
            HashSet = set()
            # 从当前位置pos往下遍历
            for i in range(pos,len(c)):
                # 如果遍历到的位置在集合中，说明之前的遍历中这个字符放在过pos的位置上
                if c[i] in HashSet: continue
                # 哈希集合增加
                HashSet.add(c[i])
                # 交换位置
                c[i], c[pos] = c[pos], c[i]
                # 往下dfs
                dfs(pos+1)
                # 复原位置
                c[i], c[pos] = c[pos], c[i]
        dfs(0)
        return ans
