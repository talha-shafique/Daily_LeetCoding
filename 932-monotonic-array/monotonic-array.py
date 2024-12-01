class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        print(sorted(nums))
        if nums==sorted(nums) or nums==sorted(nums, reverse=True):
            return True
        else:
            return False
        



        