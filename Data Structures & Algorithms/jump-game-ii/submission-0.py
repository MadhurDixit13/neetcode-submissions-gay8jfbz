class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [len(nums)]*len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            if(dp[i] > i):
                dp[i] = i
            if (i+nums[i] >=len(nums)):
                dp[len(nums)-1] = min(dp[len(nums)-1], dp[i] + 1)
            else:
                dp[i+nums[i]] = min(dp[i+nums[i]], dp[i] + 1)
            
        return dp[len(nums)-1]