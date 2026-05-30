class Solution:
    def sum(self, r):
        s = 0
        for i in range(len(r)):
            # 1. FIXED: Changed addition to multiplication to SQUARE the digits
            s = s + r[i] * r[i]
        return s

    def isHappy(self, n: int) -> bool:
        res = []
        while len(res) == len(set(res)):
            li = list(str(n))
            ln = []
            for i in range(len(li)):
                ln.append(int(li[i]))
            sums = self.sum(ln)
            if sums == 1:
                return True     
            res.append(sums)
            n = sums
        return False