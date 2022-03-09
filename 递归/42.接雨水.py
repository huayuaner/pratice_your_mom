# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
# 示例 2：
#
# 输入：height = [4,2,0,3,2,5]
# 输出：9

# 单调栈
# stack = []
# ans = 0
# for i in range(len(height)):
#     while stack and height[stack[-1]] < height[i]:
#         bottom = stack.pop()
#         if not stack:
#             break
#         left = stack[-1]
#         width = i - stack[-1] -1
#         high = min(height[left], height[i]) - height[bottom]
#         #print(width, high)
#         ans += width * high
#     stack.append(i)
# return ans

# 双指针
n = len(height)
left, right = 0, n - 1
LeftMax, RightMax = 0, 0
ans = 0
while left < right:
    LeftMax = max(LeftMax, height[left])
    RightMax = max(RightMax, height[right])
    if LeftMax < RightMax:
        ans += LeftMax - height[left]
        left += 1
    else:
        ans += RightMax - height[right]
        right -= 1
return ans