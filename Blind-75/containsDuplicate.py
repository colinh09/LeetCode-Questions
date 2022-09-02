class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # constraints says that nums.length can be 1 to 10^5
        if len(nums) == 1:
            return False
        # just use a hashmap. Provides constant time look up, so there's nothing
        # better to use. Maybe use the set datastructure since it only allows unique values. But I basically do that by providing a check for that with my dictionary
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = True
            else:
                return True
        return False
        
