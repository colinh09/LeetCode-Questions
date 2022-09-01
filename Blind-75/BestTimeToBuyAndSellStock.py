class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    # brute force method, results in run time error, try to optimize from this solution
        
        # p1, p2 = 0, 1
        # ans = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[i] < prices[j]:
        #             ans = max(ans, prices[j] - prices[i])
        # return ans
                    
        # improved brute force method using 2 pointers. This was still pretty slow, but did not result in a runtime error
        # p1, p2 = 0, 1
        # ans = 0
        # while p2 < len(prices):
        #     if prices[p1] > prices[p2]:
        #         p1 = p2
        #         p2 += 1
        #     else:
        #         ans = max(ans, prices[p2] - prices[p1])
        #         p2 += 1
        # return ans
        
        # much faster soln by just looping through prices once, keeping track of the minimum price encountered, and just updating ans and minprice as smaller values are being found. 
        min_price, ans = float(inf), 0
        for i in prices:
            if i < min_price:
                min_price =  i
            else:
                ans = max(ans, i - min_price)
        return ans
