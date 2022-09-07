class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # main idea: to not use the division operator while solving this problem in O(n) time, we need to set up a prefix and a postfix for every calculation and store them in arrays. For example, in the array [1,2,3,4], the prefix for 3 would be 2 and the postfix would be 4, resulting in the answer 8.
        # However, this would require two arrays, one for postfix and one for prefix, which does not satisfy the follow up question of solving the problem in O(1) space complexity. Since the output array does not account for the total space used, we can store the prefix and post fix in the output array.
        prefix, postfix = 1, 1
        ans = [1] * len(nums)
        # we want store the prefix of each number in nums. The first element of nums would just have a prefix of 1. 
        for i in range(len(nums)):
            ans[i] = prefix
            # update the prefix for the next element by multipying it by the current element in nums
            prefix *= nums[i]
        # now we are doing the postfix. The last element of nums has a postfix of 1, so it stays the same. Update postfix as you loop through the output array
        for j in range(len(nums) - 1, -1 , -1):
            # postfix * the prefix stored in the previous loop
            ans[j] *= postfix
            # update postfix as you iterate through the ans array
            postfix *= nums[j] 
        return ans
            
