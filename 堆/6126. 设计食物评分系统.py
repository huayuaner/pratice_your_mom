# 设计一个支持下述操作的食物评分系统：
#
# 修改 系统中列出的某种食物的评分。
# 返回系统中某一类烹饪方式下评分最高的食物。
# 实现 FoodRatings 类：
#
# FoodRatings(String[] foods, String[] cuisines, int[] ratings) 初始化系统。食物由 foods、cuisines 和 ratings 描述，长度均为 n 。
# foods[i] 是第 i 种食物的名字。
# cuisines[i] 是第 i 种食物的烹饪方式。
# ratings[i] 是第 i 种食物的最初评分。
# void changeRating(String food, int newRating) 修改名字为 food 的食物的评分。
# String highestRated(String cuisine) 返回指定烹饪方式 cuisine 下评分最高的食物的名字。如果存在并列，返回 字典序较小 的名字。
# 注意，字符串 x 的字典序比字符串 y 更小的前提是：x 在字典中出现的位置在 y 之前，也就是说，要么 x 是 y 的前缀，或者在满足 x[i] != y[i] 的第一个位置 i 处，x[i] 在字母表中出现的位置在 y[i] 之前。
from collections import defaultdict
import heapq


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.dic_CountrytoFood = defaultdict(list)
        self.dic_FoodtoCountry = dict()
        # self.dic_FoodtoScore = dict()
        for i in range(len(foods)):
            heapq.heappush(self.dic_CountrytoFood[cuisines[i]], (-ratings[i], foods[i]))
            # self.dic_FoodtoScore[foods[i]] = ratings[i]
            self.dic_FoodtoCountry[foods[i]] = [cuisines[i], ratings[i]]

    def changeRating(self, food: str, newRating: int) -> None:
        # self.dic_FoodtoScore[food] = newRating
        country, _ = self.dic_FoodtoCountry[food]
        heapq.heappush(self.dic_CountrytoFood[country], (-newRating, food))
        self.dic_FoodtoCountry[food][1] = newRating

    def highestRated(self, cuisine: str) -> str:
        # print(self.dic_CountrytoFood[cuisine][0][0], self.dic_FoodtoCountry[self.dic_CountrytoFood[cuisine][0][1]])
        food_l = self.dic_CountrytoFood[cuisine]
        while -food_l[0][0] != self.dic_FoodtoCountry[food_l[0][1]][1]:
            heapq.heappop(self.dic_CountrytoFood[cuisine])
        return self.dic_CountrytoFood[cuisine][0][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)