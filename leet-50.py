#******************************递归************************************8
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         def pp(x:float, n:int):
#             if (n<=1):
#                 return x
#             temp = pp(x, n//2)
#             if(n%2 == 0):
#                 res = temp*temp
#             else:
#                 res = temp*temp*x
#             return res
#         if n>0:
#             return pp(x, n)
#         elif n<0:
#             tt = pp(x, -n)
#             return 1 / tt
#         else:return 1


def myPow(x: float, n: int) -> float:
    flag =1
    kk = 1
    res =0
    while(n>=1):
        temp = n%2
        n=n//2
        kk = kk*x
        if flag:
            kk=1
            flag=0
        if temp == 1:
            res*=kk
    return res

a =myPow(2,10)