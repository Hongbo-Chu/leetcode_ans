# ##1暴力搜索
# def L(num, i)->int:
#     #返回从第i个数字开始的最大长度
#     #用递归的方法
#     if i == len(num)-1:
#         return 1
#     max_len = 1
#     for j in range(i+1, len(num)):
#         if num[j]>num[i]:
#             ##递归的话假设已经获得了从num[i+1]开始的最大子串
#             max_len = max(max_len, 1 + L(num, j))
#     return max_len
#
# def solve(num):
#     return max(L(num,i) for i in range(len(num)))
#
#
# numss = [1,5,2,4,3]
# print(solve(numss))
#**********************************************************************************************************************************

#
# #改进
# ##就是动态规划，也成为记忆化搜索
# ##2暴力搜索改进：将遍历过的点存下来避免二次遍历
# memo ={}
# def L(num, i)->int:
#     #返回从第i个数字开始的最大长度
#     #用递归的方法
#     if i in memo:
#         return memo[i]
#     if i == len(num)-1:
#         return 1
#     max_len = 1
#     for j in range(i+1, len(num)):
#         if num[j]>num[i]:
#             ##递归的话假设已经获得了从num[i+1]开始的最大子串
#             max_len = max(max_len, 1 + L(num, j))
#     memo[i] = max_len
#     return max_len
#
# def solve(num):
#     return max(L(num,i) for i in range(len(num)))
#
#
# numss = [1,5,2,4,3]
# print(solve(numss))

#**********************************************************************************************************************************

#非递归实现
