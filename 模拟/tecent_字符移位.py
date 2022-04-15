# 小Q最近遇到了一个难题：把一个字符串的大写字母放到字符串的后面，各个字符的相对位置不变，且不能申请额外的空间。
# 你能帮帮小Q吗？
# 利用类似冒泡排序法的方法对字符进行移位
def helper(s):
    n = len(s)
    for i in range(n - 1, -1, -1):
        if 'A' <= s[i] <= 'Z':
            for j in range(i + 1, n):
                if 'a' <= s[j] <= 'z':
                    s[j], s[j - 1] = s[j - 1], s[j]
    return ''.join(s)


while 1:
    try:
        s = list(input().strip())
        print(helper(s))
    except:
        break