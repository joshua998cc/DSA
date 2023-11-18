#comparing anagrams which are two strings with the same characters. return true if they are the same false if otherwise.
# going to loop through collecting both list of strings using the get function that way we can just loop once through.
#the compare the two using the get function for t and if they are equal return True. Otherwise False can compare the length of both at
#the beginning to automatically disqualify if not the same length.
class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False

        s_count, t_count = {}, {}

        for letters in range(len(s)):
            s_count[s[letters]] = 1 + s_count.get(s[letters], 0)
            t_count[t[letters]] = 1 + t_count.get(t[letters], 0)

        for x in s_count:
            if s_count[x] != t_count.get(x, 0):
                return False
        return True
    

# Test cases
solution = Solution()
test1 = solution.isAnagram("listen", "silent") #should return True
print(test1) 

test2 = solution.isAnagram("hello", "world") #should return False
print(test2) 

test3 = solution.isAnagram("adgjlkhfs", "sfhkljgda") #should return True
print(test3)
