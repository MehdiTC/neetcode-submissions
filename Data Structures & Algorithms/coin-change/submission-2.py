class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}

        def dp(amount):
            if amount==0: return 0
            if amount in memo: return memo[amount]

            res = float('inf')

            for coin in coins:
                if amount-coin>=0:
                    used = 1 + dp(amount-coin)
                    res = min(res, used)
            memo[amount] = res
            return res
        
        minCoins = dp(amount)
        return -1 if minCoins == float('inf') else minCoins
                
        