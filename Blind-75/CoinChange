class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # we want to initialize a cache with length amount+1 such that the
        # last element of the array is our answer. We also initalize each element
        # value to amount+1 because no coin amount is going to exceed amount+1
        dp = [amount+1] * (amount+1)
        # it takes 0 coins to get to 0, base case
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                # need to make sure that we are not going exceeding the amount
                if i - coin >= 0:
                    # we are iterating through each coin value in coins
                    # dp[i] should hold the the least # of coins to get to amount
                    # the 1 comes from the ONE coin we are adding while dp[i-c] is
                    # the leftover amount we are trying to find
                    # ex. coin = 4, amount = 7, therefore, we need the four coin
                    # plus the amount of coins it took to get to the amount 7-4.
                    dp[i] = min(dp[i], 1 + dp[i-coin])
        # there is a possibility that none of the coin arrangements matches the 
        # target amount value. We ensure that dp[amount] will = amount + 1 with
        # the i - coin >= 0 condition.
        return dp[amount] if dp[amount] != amount + 1 else -1
