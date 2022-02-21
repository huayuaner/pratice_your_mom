假设你是一位顺风车司机，车上最初有 capacity 个空座位可以用来载客。由于道路的限制，车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向，你可以将其想象为一个向量）。

这儿有一份乘客行程计划表 trips[][]，其中 trips[i] = [num_passengers, start_location, end_location] 包含了第 i 组乘客的行程信息：

必须接送的乘客数量；
乘客的上车地点；
以及乘客的下车地点。
这些给出的地点位置是从你的 初始 出发位置向前行驶到这些地点所需的距离（它们一定在你的行驶方向上）。

请你根据给出的行程计划表和车子的座位数，来判断你的车是否可以顺利完成接送所有乘客的任务（当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false）。
示例 1：

输入：trips = [[2,1,5],[3,3,7]], capacity = 4
输出：false
示例 2：

输入：trips = [[2,1,5],[3,3,7]], capacity = 5
输出：true
示例 3：

输入：trips = [[2,1,5],[3,5,7]], capacity = 3
输出：true
示例 4：

输入：trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
输出：true
 
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        f = [0 for _ in range(1001)]
        for x, up, down in trips:
            # 记录每个时间点上下车的人数
            f[up] += x
            f[down] -= x 
        # 计算每个时间点车上的人数
        if f[0]>capacity:
            return False
        for i in range(1, 1001):
        
            f[i] = f[i-1] + f[i]
            if f[i]> capacity:
                return False
        return True

# 模拟2
        # 以出发点排序
        trips.sort(key=lambda x:x[1])
        # 用小根堆找到当前终点最近的一单
        heap_end = []
        cnt = 0
        for i in range(len(trips)):
            # 弹出当前开始时已经下车的人
            while heap_end and trips[i][1] >= heap_end[0][0]:
                end, passengers = heappop(heap_end)
                cnt -= passengers
            # 加入当前上车的人
            cnt += trips[i][0]
            if cnt > capacity:
                return False
            # 将终点和乘客数放入小根堆
            heappush(heap_end, [trips[i][2], trips[i][0]])
        return True 
            