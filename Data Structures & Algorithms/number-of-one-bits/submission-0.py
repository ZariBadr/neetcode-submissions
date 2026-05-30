class Solution:
    def hammingWeight(self, n: int) -> int:
        r = 0
        for i in range(32):
            if (1 << i) & n:
                r += 1
        return r