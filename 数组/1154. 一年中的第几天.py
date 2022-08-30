# 给你一个字符串 date ，按 YYYY-MM-DD 格式表示一个 现行公元纪年法 日期。返回该日期是当年的第几天。
#
#  
#
# 示例 1：
#
# 输入：date = "2019-01-09"
# 输出：9
# 解释：给定日期是2019年的第九天。
# 示例 2：
#
# 输入：date = "2019-02-10"
# 输出：41

class Solution:
    def dayOfYear(self, date: str) -> int:
        # dic = {1:31,2:28,3:31,4:30, 5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        # y_m_d = list(map(int, date.split('-')))
        # if (y_m_d[0]%4 ==0 and y_m_d[0]%100!=0) or (y_m_d[0]%400==0):
        #     run = True
        # else:
        #     run = False
        # days = 0
        # for i in range(y_m_d[1]-1):
        #     days += dic[i+1]
        # days += y_m_d[2]
        # if y_m_d[1]>2 and run:
        #     days += 1
        # return days

        # 优雅写法
        year, month, day = map(int, date.split('-'))
        amount = [31,28,31,30,31,30,31,31,30,31,30,31]
        if (year%4 ==0 and year%100!=0) or (year%400==0):
            amount[1] += 1
        return sum(amount[:month-1])+day

