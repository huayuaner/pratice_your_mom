# 给定2D空间中四个点的坐标 p1, p2, p3 和 p4，如果这四个点构成一个正方形，则返回 true 。
#
# 点的坐标 pi 表示为 [xi, yi] 。输入 不是 按任何顺序给出的。
#
# 一个 有效的正方形 有四条等边和四个等角(90度角)。
#
from collections import Counter
import math


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # standard = None
        # for p_1 in [p1,p2,p3,p4]:
        #     cnt = Counter()
        #     for p_2 in [p1,p2,p3,p4]:
        #         if p_1 == p_2: continue
        #         # 计算每一个点和其他点的距离
        #         length = abs(p_1[0]-p_2[0])**2 + abs(p_1[1] - p_2[1])**2
        #         cnt[length] += 1
        #     # 如果长度不是两种
        #     if len(cnt)!=2:return False
        #     key1, key2 = cnt.keys()
        #     # 如果长度的对应关系不是两倍
        #     if key1 != 2*key2 and key2!=2*key1:return False
        #     # 如果长度的对应数量不满足要求
        #     if (cnt[key1]!=1 and cnt[key2]!=2) and (cnt[key1]!=2 and cnt[key2]!=1):return False
        #     # 如果标准为空，以此cnt为标准
        #     if standard == None:
        #         standard = cnt
        #     # 否则进行比较
        #     else:
        #         if standard!=cnt:
        #             return False
        # return True

        def dis(p1, p2):
            return abs(p1[0] - p2[0]) ** 2 + abs(p1[1] - p2[1]) ** 2

        edge_list = list()
        edge_list.append(dis(p1, p2))
        edge_list.append(dis(p1, p3))
        edge_list.append(dis(p1, p4))
        edge_list.append(dis(p2, p3))
        edge_list.append(dis(p2, p4))
        edge_list.append(dis(p3, p4))
        unique_edge = set(edge_list)
        if len(unique_edge) == 2 and 0 not in unique_edge:
            return True
        return False
