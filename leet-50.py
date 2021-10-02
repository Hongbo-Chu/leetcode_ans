class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pp(x:float, n:int):
            if (n<=1):
                return x
            temp = pp(x, n//2)
            if(n%2 == 0):
                res = temp*temp
            else:
                res = temp*temp*x
            return res
        if n>0:
            return pp(x, n)
        elif n<0:
            tt = pp(x, -n)
            return 1 / tt
        else:return 1