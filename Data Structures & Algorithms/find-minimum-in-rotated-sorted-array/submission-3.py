class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        start = nums[0]

        while l<r:
            m = l + (r-l)//2

            if nums[m] < start:
                r = m 
            else: 
                l = m+1

        
        if nums[l]>start:
            return start

        return nums[l]
