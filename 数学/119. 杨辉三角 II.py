class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for i in range(1, rowIndex+1):
            ans.append(ans[-1]*(rowIndex-i+1)//i)
        return ans
