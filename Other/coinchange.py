from collections import deque
class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
            print(dp)
        return dp[amount] if dp[amount] != float('inf') else -1 
    
class Solution1:
    def coinChange(self, coins, amount: int) -> int:
        dq = deque([(amount,0)])
        seen = set([amount])
        
        while dq:
            accum_amount, num_coins = dq.popleft()
            if accum_amount == 0:
                return num_coins
            for coin in coins:
                if accum_amount-coin >= 0 and accum_amount-coin not in seen:
                    dq.append((accum_amount-coin, num_coins+1))
                    seen.add(accum_amount - coin)
        return -1

print(Solution1().coinChange([1,2,5], 11))