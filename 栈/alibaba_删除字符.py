#有一个长度为N的字符串 ，你可以删除其中的m个字符，使剩余字符串的字典序最小，输出这个剩余字符串。


17
n = int(input())
# ans = []
stack = []
for _ in range(n):
    stack.clear()
    _, d = list(map(int, input().split()))
    s = str(input())
    for c in s:
        # 删除逆序的
        while stack and stack[-1] > c and d:
            stack.pop()
            # 可用删除-1
            d -= 1
        stack.append(c)
    if d == 0:
        print(''.join(stack))
    else:
        print(''.join(stack[:-d]))
