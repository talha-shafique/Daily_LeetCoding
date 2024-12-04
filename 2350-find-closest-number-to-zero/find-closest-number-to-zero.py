class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort(reverse =True)
        res=[]
        for i in nums:
            dis=abs(i)-0
            res.append(dis)
        return nums[res.index(min(res))]




    


        