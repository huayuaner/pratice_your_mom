# 给你一个日志数组 logs。每条日志都是以空格分隔的字串，其第一个字为字母与数字混合的 标识符 。
#
# 有两种不同类型的日志：
#
# 字母日志：除标识符之外，所有字均由小写字母组成
# 数字日志：除标识符之外，所有字均由数字组成
# 请按下述规则将日志重新排序：
#
# 所有 字母日志 都排在 数字日志 之前。
# 字母日志 在内容不同时，忽略标识符后，按内容字母顺序排序；在内容相同时，按标识符排序。
# 数字日志 应该保留原来的相对顺序。
# 返回日志的最终顺序。
#
#  
#
# 示例 1：
#
# 输入：logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# 输出：["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
# 解释：
# 字母日志的内容都不同，所以顺序为 "art can", "art zero", "own kit dig" 。
# 数字日志保留原来的相对顺序 "dig1 8 1 5 1", "dig2 3 6" 。
# 示例 2：
#
# 输入：logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# 输出：["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
#
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # alpha = []
        # number = []
        # for log in logs:
        #     if log[-1].isdigit():
        #         number.append(log)
        #     else:
        #         alpha.append(log)
        # alpha.sort(key=lambda x:((x[x.find(' ')+1:], x[:x.find(' ')])))
        # return alpha+number

        def trans(log: str) -> tuple:
            a, b = log.split(' ', 1)
            # print(a,' ', b)
            # 如果是字母日志 就返回(0,b,a)表示先比较 0, 如果相同就比较b，再相同就比较 a
            # 如果是数字日志 就返回(1,)这样就不用比较了，保持原有的顺序
            return (0, b, a) if b[0].isalpha() else (1,)

        logs.sort(key=trans)  # sort 是稳定排序
        return logs




