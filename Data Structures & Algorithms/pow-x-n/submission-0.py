class Solution:
    def myPow(self, x: float, n: int) -> float:
        acc = 1
        if n < 0:
            n = -n
            while n > 0:
                acc = acc * x
                n = n - 1
            return 1 / acc
        while n > 0:
            acc = acc * x
            n = n - 1
        return acc
        