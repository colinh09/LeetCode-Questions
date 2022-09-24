class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # in this problem, it is intutive that if the preceeding sum of elements before the element we are currently on is negative, it will not contribute to the largest sum
        # therefore, we keep track of the prefix, and only continue if it is positive. If it is negative, set it back to 0. 
       #This is essentially skipping all of the elements contributing to the negative prefix and continuing onto the next subarray.
        
        # we also see that we need to keep track of a max value. There are multiple subarrays that can have positive values. Obviously need to keep track of the max one
        # we see this in the first example they give us: nums = [-2,1,-3,4,-1,2,1,-5,4] where [4, -1, 2, 1] has a higher sum than [4,-1,2,1,-5,4].
        maxVal = float('-inf')
        prefix = 0
        for i in nums:
            if prefix < 0:
                prefix = 0
            prefix += i
            if prefix > maxVal:
                maxVal = prefix
        return maxVal

    # decided to also explore the divide and conquer solution
    # I feel like this solution is not as intuitive. You start from the middle, but exclude the middle
    # take the best left sum and best right sum. Add them together with the middle. That is your max sub array.
    # really unintutive imo unless you prove it to yourself on paper
    
    def findBestSubarray(nums, left, right):
            # if the array is empty
            if left > right:
                return -math.inf
            # left + right / 2 rounded down
            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            # middle to left
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            # middle to right
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            # middle + best right sum + best left sum
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            # recursively call the function in case there is a better sum in either of the halves of num
            # this actually answers my question about the unintuitiveness of this solution. I think leetcode fails to explain these recursive calls.
            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)

            # returns the highest value
            return max(best_combined_sum, left_half, right_half)
        
        # Our helper function is designed to solve this problem for
        # any array - so just call it using the entire input!
        return findBestSubarray(nums, 0, len(nums) - 1)
