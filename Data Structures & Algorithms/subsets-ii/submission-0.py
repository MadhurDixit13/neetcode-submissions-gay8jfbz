class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        def backtrack(start, temp):
            ans.append(list(temp))  # include current subset
            
            for i in range(start, len(nums)):
                # skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                temp.append(nums[i])
                backtrack(i + 1, temp)
                temp.pop()

        backtrack(0, [])
        return ans

            