class Solution:
    def rob(self, nums: List[int]) -> int:
        # for reference rob1 and rob2 are the previous 2 houses before n in the for loop
        # for example [rob1, rob2, n, n+1, ....]
        rob1, rob2 = 0, 0
        # for each house in nums, we can make a decision.
        # either choose to rob the house or skip it. If we choose to rob it we can add rob1 to it. If we choose to skip it, set it equal to rob 2.
        # we decide this by taking the max of i+rob1 and rob2
        # its kinda like having 2 pointers on the previous 2 houses for each house in nums and constantl updating them
        for i in nums:
            temp = max(i+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
            
            
