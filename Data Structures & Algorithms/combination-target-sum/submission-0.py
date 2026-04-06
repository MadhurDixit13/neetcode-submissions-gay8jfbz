class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(index, sum, curr):
            if index>=len(nums):
                return
            if (sum > target):
                return
            if (sum == target):
                ans.append(curr.copy())
                return
            curr.append(nums[index])
            backtrack(index, sum+nums[index], curr)
            curr.pop()
            backtrack(index+1, sum, curr)
        backtrack(0, 0 , [])
        return ans