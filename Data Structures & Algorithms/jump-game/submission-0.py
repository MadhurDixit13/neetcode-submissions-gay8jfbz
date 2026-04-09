class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        
        for n,i in enumerate(nums):
            if m < n:
                return False
            curr = n + i
            m = max(curr, m)
        
        if m >= len(nums)-1:
            return True
        return False