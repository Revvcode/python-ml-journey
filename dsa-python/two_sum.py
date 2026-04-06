# My solution to the two sum problem, brute force method and takes too long

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = []
        b = len(nums)
        for i in range (0,b):
            for j in range(0,i):
                if nums[i]+nums[j]==target:
                    a.append(i)
                    a.append(j)
                    a.sort()
                    break
        return a
    

# suggested solution, uses a sort of hash table through dictonaries

def twoSum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums): # loops through the list of numbers and their indices 
        diff = target - num # checks for complement
        
        if diff in seen:
            return [seen[diff], i]
        
        seen[num] = i # stores in the dictionary, num is the value and i is the key

# dictonary seen is used to store the numbers we have seen and diff is used to cleverly check if the complement of the current number is already seen