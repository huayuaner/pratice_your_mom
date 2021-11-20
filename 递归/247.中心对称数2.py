# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# 中心对称数是指一个数字在旋转180 度之后看起来依旧相同的数字（或者上下颠倒地看）。
#
# 找到所有长度为 n 的中心对称数。
#
# 示例 :
#
# 输入:  n = 2
# 输出: ["11","69","88","96"]




# Press the green button in the gutter to run the script.
if __name__ == '__main__':


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        dict_ = {'1': '1', '6': '9', '8': '8', '9': '6'}

        def func(x):
            if x == 0:
                return [""]
            if x == 1:
                return ['1', '8', '0']
            res = []
            for string in func(x - 2):
                for key in dict_.keys():
                    res.append(key + string + dict_[key])
                if x != n:
                    res.append('0' + string + '0')
            return res

        return func(n)
