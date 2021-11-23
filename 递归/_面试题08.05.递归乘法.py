#递归乘法。 写一个递归函数，不使用 * 运算符， 实现两个正整数的相乘。可以使用加号、减号、位移，但要吝啬一些。
def multiply(self, A: int, B: int) -> int:
    # res=0
    # round_ = min(A, B)
    # add = max(A, B)
    # for i in range(round_):
    #     res += add
    # return res
    if A == 1 or B == 1:
        return max(A, B)
    else:
        if A <= B:
            res = self.multiply(A - 1, B) + B
        else:
            res = self.multiply(A, B - 1) + A
        return res