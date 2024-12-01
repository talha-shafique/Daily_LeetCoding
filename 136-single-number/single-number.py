class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        stack=[]
        for i in nums:
            if nums.count(i)==1:
                return i

        