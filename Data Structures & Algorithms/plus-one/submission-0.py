class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = 0
        for i in range(0,len(digits)):
            digit = digit * 10 + digits[i]
        digit = digit + 1
        return list(str(digit))
            

        