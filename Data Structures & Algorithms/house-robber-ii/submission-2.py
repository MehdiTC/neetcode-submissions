class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        skipFirst = nums[1:]
        skipLast = nums[:-1]

        r1, r2 = 0, 0 
        for i in range(len(skipFirst)):
            r1, r2 = r2, max(r2, r1 + skipFirst[i])
        
        y1, y2 = 0, 0 
        for i in range(len(skipLast)):
            y1, y2 = y2, max(y2, y1 + skipLast[i])
        
        return max(y2, r2)
        

        

            