class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res, sol, sum = [], [], 0

        def backtrack():
            nonlocal sum

            if sum == target:
                res.append(sol[:])
                return
            
            for i in nums:
                if not sol or i <= sol[-1]:
                    sum+=i
                    if sum <= target:
                        sol.append(i)
                        backtrack()
                        sol.pop()
                    sum-=i
            

        backtrack()
        return res

                    




        