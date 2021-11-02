class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ##dp[x]表示取元素和为x的方案数量、
        dp = [0]*(target+1)
        #这样写的话会有越界的危险
        #当list中的数大于target的数量的时候
        # for i in range(len(nums)):
        #     dp[nums[i]] = 1
        #所以直接令dp[0] =1
        #循环的过程中，就给dp[nums]赋值了
        dp[0] = 1
        for k in range(target+1):
            for j in nums:
                if k-j>=0:
                    dp[k] +=dp[k-j]
        return dp[target]