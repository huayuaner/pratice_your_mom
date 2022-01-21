# 你的国家有无数个湖泊，所有湖泊一开始都是空的。当第 n 个湖泊下雨的时候，如果第 n 个湖泊是空的，那么它就会装满水，否则这个湖泊会发生洪水。你的目标是避免任意一个湖泊发生洪水。
#
# 给你一个整数数组 rains ，其中：
#
# rains[i] > 0 表示第 i 天时，第 rains[i] 个湖泊会下雨。
# rains[i] == 0 表示第 i 天没有湖泊会下雨，你可以选择 一个 湖泊并 抽干 这个湖泊的水。
# 请返回一个数组 ans ，满足：
#
# ans.length == rains.length
# 如果 rains[i] > 0 ，那么ans[i] == -1 。
# 如果 rains[i] == 0 ，ans[i] 是你第 i 天选择抽干的湖泊。
# 如果有多种可行解，请返回它们中的 任意一个 。如果没办法阻止洪水，请返回一个 空的数组 。
#
# 请注意，如果你选择抽干一个装满水的湖泊，它会变成一个空的湖泊。但如果你选择抽干一个空的湖泊，那么将无事发生（详情请看示例 4）。
#
#  
#
# 示例 1：
#
# 输入：rains = [1,2,3,4]
# 输出：[-1,-1,-1,-1]
# 解释：第一天后，装满水的湖泊包括 [1]
# 第二天后，装满水的湖泊包括 [1,2]
# 第三天后，装满水的湖泊包括 [1,2,3]
# 第四天后，装满水的湖泊包括 [1,2,3,4]
# 没有哪一天你可以抽干任何湖泊的水，也没有湖泊会发生洪水。
# 示例 2：
#
# 输入：rains = [1,2,0,0,2,1]
# 输出：[-1,-1,2,1,-1,-1]
# 解释：第一天后，装满水的湖泊包括 [1]
# 第二天后，装满水的湖泊包括 [1,2]
# 第三天后，我们抽干湖泊 2 。所以剩下装满水的湖泊包括 [1]
# 第四天后，我们抽干湖泊 1 。所以暂时没有装满水的湖泊了。
# 第五天后，装满水的湖泊包括 [2]。
# 第六天后，装满水的湖泊包括 [1,2]。
# 可以看出，这个方案下不会有洪水发生。同时， [-1,-1,1,2,-1,-1] 也是另一个可行的没有洪水的方案。
# 示例 3：
#
# 输入：rains = [1,2,0,1,2]
# 输出：[]
# 解释：第二天后，装满水的湖泊包括 [1,2]。我们可以在第三天抽干一个湖泊的水。
# 但第三天后，湖泊 1 和 2 都会再次下雨，所以不管我们第三天抽干哪个湖泊的水，另一个湖泊都会发生洪水。
# 示例 4：
#
# 输入：rains = [69,0,0,0,69]
# 输出：[-1,69,1,1,-1]
# 解释：任何形如 [-1,69,x,y,-1], [-1,x,69,y,-1] 或者 [-1,x,y,69,-1] 都是可行的解，其中 1 <= x,y <= 10^9
# 示例 5：
#
# 输入：rains = [10,20,20]
# 输出：[]
# 解释：由于湖泊 20 会连续下 2 天的雨，所以没有没有办法阻止洪水。

import bisect


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        #存湖泊最近下雨时间
        Rain = dict()
        #存晴天褥子
        Sunny = []
        ans = [-1] * len(rains)
        for i, rain in enumerate(rains):
            if not rain:
                Sunny.append(i)
                # 按要求转成1
                ans[i] = 1

            else:
                if rain not in Rain:
                    Rain[rain] = i

                else:
                    #该湖前一个下雨日期
                    pre = Rain[rain]
                    lens = len(Sunny)
                    #查找大于pos的第一个位置，没有则返回与Sunny长度一样的值
                    pos = bisect.bisect(Sunny, pre)
                    # 两个日期之间没有晴天可用，返回空列表
                    if pos == lens:
                        # print(pos, lens)
                        return []
                    # Sunny.pop(pos)
                    # 将该天删除，并将该天结果改成抽干的湖的名字
                    ans[Sunny.pop(pos)] = rain
                    #更新下雨日期
                    Rain[rain] = i
        return ans
