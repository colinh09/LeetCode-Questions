class Solution:
    def numDecodings(self, s: str) -> int:
        # 
        dp = {len(s) : 1}
        # bottom up dp
        # I feel like this solution is quite difficult (at least for me) to visualize unless I actually prove it on paper
        # the recursive solution is a lot more intuitive than this, but since this was more confusing I wanted to write the dp soln out
        # essentially, if there's never two set of digits within s that falls between 10 and 26 inclusive, the answer is just one
        # you can only make more mappings of characters IF there are integers that fall between 10 and 26
        # thats why we only increment dp[i] by dp[i+2] when it falls in 10 and 26 
        # I think ending this off with an example is best.
        
        # lets say we have [1 1 0]. While at 0, dp[2] will = 0. While at dp[1], dp[1] will equal d[1+1] which is dp[2] = 0. 
        # BUT since we can make the combination of 1 and 0 (10) we can add dp[1] to dp[3] which is initialized to 1 from the first statement in this soln
        # so now dp[1] = 1, but why? Thats because 0 can never stand alone. We HAVE to make 10 because 0 prohibits it.
        # now we go to dp[0]. dp[0] will get set to dp[1] = 1. But since dp[0] + dp[1] makes 11, which is valid, we can add dp[2] to dp[0]
        # but wait, dp[2] is 0, so dp[0] remains equal to 1
        # but this makes sense. If we just look at [110], we cant do [1, 1, 0], because 0 stands alone
        # we can't do [11, 0] because 0 stands alone. We MUST have [1, 10] because that 0 needs a pairing.
        # this is why we set dp[i] = dp[i+1] and dp[1] = dp[i+2]. All because 0 isn't allowed to stand alone.
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
                
            if i+1 < len(s) and int(s[i] + s[i+1]) in range(10,27):
                dp[i] += dp[i+2]
        print(dp)
        return dp[0]
