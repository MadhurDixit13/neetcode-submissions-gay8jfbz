class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        for i in nums:
            sum = sum + i
        return int((len(nums)*(len(nums)+1)/2)) - sum