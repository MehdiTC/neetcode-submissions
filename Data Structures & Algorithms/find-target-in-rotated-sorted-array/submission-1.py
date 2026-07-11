class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l<r:
            m = l + (r-l)//2

            if nums[m] < nums[r]:
                r = m 
            else: 
                l = m + 1

        print(l)
        
        if l != 0:    
            l1 = 0
            r1 = l - 1

            while l1 <= r1:
                m = l1 + (r1-l1)//2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l1 = m+1
                else:
                    r1 = m-1
        
        l2 = l
        r2 = len(nums) - 1

        while l2 <= r2:
            m = l2 + (r2-l2)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l2 = m+1
            else:
                r2 = m-1
        
        
        return -1



