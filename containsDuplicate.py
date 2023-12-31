#given an array of intergers return the True if one apprears at least twice. False if otherwise
#to loop through the array once use the set to collect each item. if the item is already in the set simply return true. if not add the number and move on the the next in the array. Once we get to the end of the array and there are no duplicates. return False
class Solution:
    def containsDuplicate(self, nums):
        group = set()

        for number in nums:
            if number in group:
                return True
            group.add(number)
        return False
    
solution_instance = Solution()

nums1 = [1,3,3,4,5,6,7,8] #should return True
result1 = solution_instance.containsDuplicate(nums1)
print(result1)

nums2 = [3,1,2,5,7,9,4] #should return False
result2 = solution_instance.containsDuplicate(nums2)
print(result2)

nums3 = [12, 0, 23, 44, 55, 82, 90, 81, 23, 77, 65] #should return True
result3 = solution_instance.containsDuplicate(nums3)
print(result3)
