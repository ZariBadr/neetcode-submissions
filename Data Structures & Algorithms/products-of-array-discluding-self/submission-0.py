class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = []
        acc = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    acc = acc * nums[j]
            prod.append(acc)
            acc = 1
        return prod