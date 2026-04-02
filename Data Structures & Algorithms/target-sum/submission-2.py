class Solution:
    def findTargetSumWays(self, nums, target):
        memo = {}

        def dp(index, total):
            if index == len(nums):
                return 1 if total == target else 0

            if (index, total) in memo:
                return memo[(index, total)]

            memo[(index, total)] = dp(index + 1, total + nums[index]) + dp(index + 1, total - nums[index])
            return memo[(index, total)]

        return dp(0, 0)