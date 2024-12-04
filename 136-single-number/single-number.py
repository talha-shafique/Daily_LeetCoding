class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s=[]
        for i in nums:
            print('ind',nums.index(i))
            if i in s:
                s.remove(i)
            else:
                s.append(i)
        print(s)
        return s[0]
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Less Efficient
        # for i in nums:
        #     if nums.count(i)==1:
        #         return i

        