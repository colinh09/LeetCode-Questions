class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # storing dp in a hashmap for constant time look up. To get the sum 0, every num is nums is positive, so its just going to be one
        dp = {0: 1}
        # want to store how many combinations we can take to each number up to target
        for i in range(1, target + 1):
            # initialize hashmap entry to 0
            dp[i] = 0
            # if you were to draw out the tree for the example they gave us (target = 4, nums = [1,2,3], it would turn out that dp[4] = dp[3]+dp[2]+dp[1] = 7)
            # which is dp[4-1] + dp[4-2] + dp[4-3]. This is what we're essentially doing for every number leading up to nums. If it DNE, add 0 bc there is no combination
            for n in nums:
                dp[i] += dp.get(i - n, 0)
        return dp[i]
            
        
                
