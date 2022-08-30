# 给你一个混合了数字和字母的字符串 s，其中的字母均为小写英文字母。
#
# 请你将该字符串重新格式化，使得任意两个相邻字符的类型都不同。也就是说，字母后面应该跟着数字，而数字后面应该跟着字母。
#
# 请你返回 重新格式化后 的字符串；如果无法按要求重新格式化，则返回一个 空字符串 。
class Solution:
    def reformat(self, s: str) -> str:
        # 计算字母和数字的个数
        # 不满足条件的话一定是False
        # cnt_alpha = cnt_digit = 0
        # alpha, digit = [], []
        # n = len(s)
        # for c in s:
        #     if c.isdigit():
        #         # cnt_digit += 1
        #         digit.append(c)
        #     else:
        #         # cnt_alpha += 1
        #         alpha.append(c)
        # if abs(len(alpha)-len(digit))>1:
        #     return ''
        # ans = [None]*n
        # if len(alpha) > len(digit):
        #     p_alpha = 0
        #     p_digit = 1
        # else:
        #     p_digit, p_alpha = 0, 1
        # for c in s:
        #     if c.isdigit():
        #         ans[p_digit] = c
        #         p_digit += 2
        #     else:
        #         ans[p_alpha] = c
        #         p_alpha += 2
        # return ''.join(ans)

        n = len(s)
        cnt_digit = sum(c.isdigit() for c in s)
        cnt_alpha = n - cnt_digit
        if abs(cnt_alpha - cnt_digit) > 1:
            return ''
        s_l = list(s)
        flag = cnt_digit > cnt_alpha
        # i遍历偶数位置
        # j遍历奇数位置
        j = 1
        for i in range(0, n, 2):
            # 这里很巧妙，如果flag为真，说明开头要是数字
            # flag为假，说明开头是字母
            if s_l[i].isdigit() != flag:
                # 位置j由于是奇数，就应该不同于flag
                while s_l[j].isdigit() != flag:
                    j += 2
                s_l[i], s_l[j] = s_l[j], s_l[i]
        return ''.join(s_l)






