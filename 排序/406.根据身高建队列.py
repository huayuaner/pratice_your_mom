# 假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，前面 正好 有 ki 个身高大于或等于 hi 的人。
#
# 请你重新构造并返回输入数组 people 所表示的队列。返回的队列应该格式化为数组 queue ，其中 queue[j] = [hj, kj] 是队列中第 j 个人的属性（queue[0] 是排在队列前面的人）。
#
#  
#
# 示例 1：
#
# 输入：people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# 输出：[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
# 解释：
# 编号为 0 的人身高为 5 ，没有身高更高或者相同的人排在他前面。
# 编号为 1 的人身高为 7 ，没有身高更高或者相同的人排在他前面。
# 编号为 2 的人身高为 5 ，有 2 个身高更高或者相同的人排在他前面，即编号为 0 和 1 的人。
# 编号为 3 的人身高为 6 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
# 编号为 4 的人身高为 4 ，有 4 个身高更高或者相同的人排在他前面，即编号为 0、1、2、3 的人。
# 编号为 5 的人身高为 7 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
# 因此 [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] 是重新构造后的队列。
# 示例 2：
#
# 输入：people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
# 输出：[[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 按照身高从大到小排序，k从小到大排序
        people.sort(key=lambda x: (-x[0], x[1]))
        # print(people)
        n = len(people)
        ans = list()
        # 将每一个person 插入到person[1]的位置
        # 首先每次会先从身高高的插入，所以后面身高低的并不影响之前插入的人
        # 所以只需要每个都插入到前面应该有的person[i]的位置即可，因为之前插入的身高都大于等于当前身高
        for person in people:
            # print(person[1])
            ans.insert(person[1], person)
            # print(ans)
        return ans


