#*********************************************分治算法***********************************************************
# class struct:
#     def __init__(self, a):
#         self.lsum = a
#         self.rsum = a
#         self.asum = a  # 全列和
#         self.msum = a  # 最大和
# class Solution:
#     def maxSubArray(self, nums: list[int]) -> int:
#         def solve(nums, lo, hi) ->struct:
#             if(lo == hi):
#                 kk = struct(nums[lo])
#                 return kk
#             mid = (lo+hi)//2
#             left = solve(nums, lo, mid)
#             right = solve(nums, mid+1, hi)
#             temp =  struct(0)
#             temp.lsum = max(left.asum+right.lsum, left.lsum)
#             temp.rsum = max(right.asum+left.rsum, right.rsum)
#             temp.asum = left.asum+right.asum
#             temp.msum = max(left.rsum+right.lsum, left.msum, right.msum)
#             return temp
#         tt = solve(nums)
#         kk = tt.msum
#         return kk


#*****************************************动态规划*******************************************************************
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        pre =0
        max_sum = nums[0]
        for i in range(len(nums)):
            pre = max(nums[i], pre+nums[i])
            max_sum = max(max_sum, pre)
        return max_sum

