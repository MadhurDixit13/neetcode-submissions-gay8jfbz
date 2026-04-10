from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()  # Sort to group duplicates together
        
        def backtrack(index, temp, current_sum):
            if current_sum == target:
                ans.append(temp.copy())
                return
            if current_sum > target or index >= len(candidates):
                return
            
            # Include candidates[index]
            temp.append(candidates[index])
            backtrack(index + 1, temp, current_sum + candidates[index])
            temp.pop()
            
            # Skip candidates[index] AND all its duplicates
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            backtrack(index + 1, temp, current_sum)
        
        backtrack(0, [], 0)
        return ans