class Solution:
    def rob(self, nums: List[int]) -> int:  
        # theres not much to say for this problem.
        # since the house are now arranged in a circle, you cannot rob the first and last house in nums
        # therefore, you must rob either houses nums[0] to nums[len(nums)-1] or nums[1] to nums[len(nums)]
        # put the solution from house robber into a function, and take the max of the two house robbing options
        def robHouses(start, end, nums):
            p1, p2 = 0, 0
            for i in range(start, end):
                temp = max(nums[i] + p1, p2)
                p1 = p2
                p2 = temp
            return p2
        if len(nums) == 1:
            return nums[0]
        else:
            return max(robHouses(0, len(nums)-1, nums), robHouses(1, len(nums), nums))
