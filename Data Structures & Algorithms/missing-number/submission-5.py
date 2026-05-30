class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        start = 0
        for i in range(len(nums)):
            if start != nums[i]:
                return start
            start = start + 1
        return start