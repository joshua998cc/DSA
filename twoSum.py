#two sum return the indicis of the two numbers that add up to the target.
#optimal way is to loop through the array once subtracting each element from the target and putting it in hashmap using the enumerate method. 
#if two target are in the hashmap we will be returning the two indexes. d
class Solution:
    def twoSum(self, nums, target):
        group = {} # value, index

        for value, index in enumerate(nums):
            diff = target - index
            if diff in group:
                return [group[diff], value]
            group[index] = value


solution = Solution() 
nums1 = [1,2,3,4,5] #two solutions however will print 1 and 2 because the are the first two to pass when iterating through.
total1 = 5
result1 = solution.twoSum(nums1, total1)
print(result1)

nums2 = [2,5,9,13,6,7,12,15] # should return 6, and 7
total2 = 27
result2 = solution.twoSum(nums2, total2)
print(result2)

nums3 = [45, 30, 22, 11, 18, 16, 3] # should return 3 and 6
total3 = 14
result3 = solution.twoSum(nums3, total3)
print(result3)
