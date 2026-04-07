class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
             if nums[i]==nums[j]:
                c+=1
        if c>0:
            return True
        else:
            return False
        
# My solution to the proiblem, brute forced again and takes too long

# Python only joke solution
class Solution(object):
    def containsDuplicate(self, nums):
        return len(set(nums)) < len(nums)
    
# correct solution
# uses hashset approach where we use a set and add the value we've already seen and if we encouter it again we simply exit, else we add it to the set and continue

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False