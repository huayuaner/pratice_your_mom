class Solution:
    def countBits(self, n: int) -> List[int]:
        # return [num.bit_count() for num in range(n+1)]
        ans = []
        for i in range(n+1):
            cnt = 0
            while i:
                i &= i-1
                cnt += 1
            ans.append(cnt)
        return ans