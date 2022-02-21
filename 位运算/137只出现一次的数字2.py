给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

 

示例 1：

输入：nums = [2,2,3,2]
输出：3
示例 2：

输入：nums = [0,1,0,1,0,1,99]
输出：99

        # 位运算
        cnt = [0 for _ in range(32)]
        for num in nums:
            for i in range(32):
                if (num >> i)&1:
                    # i=0是第一位
                    cnt[i] += 1
        ans = 0
        # 负数以补码的方式存在系统中
        for i in range(32):
            if cnt[i]%3==1:
                # 符号位，这是一个负数
                if i == 31:
                    print((1<<i),ans)
                    ans -= (1<<i)
                else:
                    
                    ans |=(1<<i)
                    print(ans)
        return ans