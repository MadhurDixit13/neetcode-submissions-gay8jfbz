class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = math.floor(len(nums)/2)
        l = 0 
        r = len(nums) - 1
        while l<=r:
            if target < nums[mid]:
                r = mid-1
            elif target > nums[mid]:
                l = mid+1
            else:
                return mid
            mid = math.floor((l+r+1)/2)
        return -1