class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = len(nums)
        ans = 0
        def backtrack(index, sum):
            if index == s:
                if sum == target:
                    return 1
                else: 
                    return 0
            return backtrack(index+1, sum + nums[index]) + backtrack(index+1, sum - nums[index])
        
        return backtrack(0, 0)
                