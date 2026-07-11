class Solution:
    def findMin(self, nums: List[int]) -> int:
        answer = 1001
        for i in nums:
            if i < answer:
                answer = i 
        return answer