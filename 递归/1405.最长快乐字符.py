如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。

给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s：

s 是一个尽可能长的快乐字符串。
s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。
s 中只含有 'a'、'b' 、'c' 三种字母。
如果不存在这样的字符串 s ，请返回一个空字符串 ""。

 

示例 1：

输入：a = 1, b = 1, c = 7
输出："ccaccbcc"
解释："ccbccacc" 也是一种正确答案。
示例 2：

输入：a = 2, b = 2, c = 1
输出："aabbc"
示例 3：

输入：a = 7, b = 1, c = 0
输出："aabaa"
解释：这是该测试用例的唯一正确答案。

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # big = []
        # if a>0:
        #     heappush(big,(-a,'a'))
        # if b>0:
        #     heappush(big,(-b,'b'))
        # if c>0:
        #     heappush(big,(-c,'c'))
        # ans = ""
        # while big:
        #     cnt, char = heappop(big)
        #     cnt = -cnt
        #     if len(ans)<2 or ans[-1]!=char or ans[-2]!=char:
        #         ans += char
        #         cnt -= 1
        #         if cnt > 0:
        #             heappush(big,(-cnt,char))
        #     else:
        #         if big:
        #             cnt_1, char_1 = heappop(big)
        #             cnt_1 = -cnt_1
        #             heappush(big,(-cnt,char))
        #             ans += char_1
        #             cnt_1 -= 1
        #             if cnt_1>0:
        #                 heappush(big,(-cnt_1,char_1))
        #         else:
        #             break
        # return ans

        # 递归
        def addChars(queue, strs):
            val, char = heapq.heappop(queue)
            if not val or (len(strs) >= 2 and strs[-2] == strs[-1] == char and (not queue or not addChars(queue, strs))):
                return False
            strs.append(char)
            heapq.heappush(queue, (val + 1, char))
            return True

        pq = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapq.heapify(pq)
        ans = []
        while pq and addChars(pq, ans):
            pass
        return "".join(ans)

                    




            
                