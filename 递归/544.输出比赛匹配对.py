# 在 NBA 季后赛中，我们总是安排较强的队伍对战较弱的队伍，例如用排名第 1 的队伍和第 n 的队伍对决，这是一个可以让比赛更加有趣的好策略。现在，给你 n 支队伍，你需要以字符串格式输出它们的 最终 比赛配对。
#
# n 支队伍按从 1 到 n 的正整数格式给出，分别代表它们的初始排名（排名 1 最强，排名 n 最弱）。我们用括号（'(', ')'）和逗号（','）来表示匹配对——括号（'(', ')'）表示匹配，逗号（','）来用于分割。 在每一轮的匹配过程中，你都需要遵循将强队与弱队配对的原则。
#
# 输入: 8
# 输出: (((1,8),(4,5)),((2,7),(3,6)))
# 解析:
# 第一轮: (1,8),(2,7),(3,6),(4,5)
# 第二轮: ((1,8),(4,5)),((2,7),(3,6))
# 第三轮 (((1,8),(4,5)),((2,7),(3,6)))
# 由于第三轮会决出最终胜者，故输出答案为(((1,8),(4,5)),((2,7),(3,6)))。

def findContestMatch(self, n: int) -> str:
    def func(x):
        if x == 2:
            i, j = 1, n
            res = []
            while (i < j):
                res.append('({},{})'.format(i, j))
                i += 1
                j -= 1
            return res
        res = []
        temp = func(x / 2)
        i, j = 0, len(temp) - 1
        while (i < j):
            res.append('({},{})'.format(temp[i], temp[j]))
            i += 1
            j -= 1
        return res

    joint = ','
    return joint.join(func(n))


