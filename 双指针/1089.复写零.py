# 给你一个长度固定的整数数组 arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。
#
# 注意：请不要在超过该数组长度的位置写入元素。
#
# 要求：请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。
#
#  
#
# 示例 1：
#
# 输入：[1,0,2,3,0,4,5,0]
# 输出：null
# 解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]
# 示例 2：
#
# 输入：[1,2,3]
# 输出：null
# 解释：调用函数后，输入的数组将被修改为：[1,2,3]
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # length = len(arr)
        # i = 0
        # cnt = 0
        # while i<length-1:
        #     if arr[i] == 0:
        #         arr.insert(i,0)
        #         cnt += 1
        #         i += 1

        #     i += 1
        # while cnt:
        #     arr.pop()
        #     cnt -= 1

        # 双指针
        n = len(arr)
        i = top = 0
        while top < n:

            top += (1 if arr[i] else 2)
            # 如果top此时已经超过了top，就不再加了
            if top < n:
                i += 1
        # i -= 1
        # print(top, i,n )
        j = n - 1
        # 说明 n-1 位置是0
        if top == n + 1:
            arr[j] = 0
            j -= 1
            i -= 1
        # i的位置指向当前要放的值
        # j指向要放的位置
        while j >= 0:

            if arr[i] == 0:
                arr[j] = 0
                arr[j - 1] = 0
                j -= 2
            else:
                arr[j] = arr[i]
                j -= 1
            i -= 1



