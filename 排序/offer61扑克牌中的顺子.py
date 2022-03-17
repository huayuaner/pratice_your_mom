# 从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。
#
#  
#
# 示例 1:
#
# 输入: [1,2,3,4,5]
# 输出: True
#  
#
# 示例 2:
#
# 输入: [0,0,1,2,5]
# 输出: True
#
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        # 除0之外 最大值最小值之差不超过 5 - 鬼的数量
        # 记录鬼的数量
        # MAX, MIN = 0, 14
        # repeat = set()
        # for num in nums:
        #     if num == 0: continue
        #     MIN = num if num < MIN else MIN
        #     MAX = num if num > MAX else MAX
        #     if num in repeat: return False
        #     repeat.add(num)
        # # print(MAX,MIN)
        # return  MAX-MIN < 5

        # 排序
        cnt = 0
        nums.sort()
        for i in range(4):
            if nums[i] == 0:
                cnt += 1
            elif nums[i] == nums[i + 1]:
                return False
        return nums[-1] - nums[cnt] < 5
