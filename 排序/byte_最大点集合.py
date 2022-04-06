# P为给定的二维平面整数点集。定义 P 中某点x，如果x满足 P 中任意点都不在 x 的右上方区域内（横纵坐标都大于x），则称其为“最大的”。求出所有“最大的”点的集合。（所有点的横坐标和纵坐标都不重复, 坐标轴范围在[0, 1e9) 内）
#
# 如下图：实心点为满足条件的点的集合。请实现代码找到集合 P 中的所有 ”最大“ 点的集合并输出。

# 接收输入
pointNum = int(input())
pointList = []
for i in range(pointNum):
    pointList.append(input())
# 按y轴从大到小排序
pointList.sort(key=lambda x:int(x.split()[1]), reverse=True)
max = 0
for i in range(len(pointList)):
    # 遍历 当x出翔更大值就输出
    # 因为y从大到小，说明y比他大的点x都不比他大
    if int(pointList[i].split()[0]) >= max:
        max = int(pointList[i].split()[0])
        print(pointList[i])