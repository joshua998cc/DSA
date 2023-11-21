#Group Anagrams
# basically going to loop through all the strings and sort all of which putting together the anagrams.
#then going to append to dictionary and return the values.

# Here, a defaultdict is created using the collections module. A defaultdict is like a regular dictionary, but it has a default value for each key if it's not present. In this case, the default value is an empty list. This dictionary (dict) will be used to store groups of anagrams.

import collections

class Solution:
    def groupAnagrams(self, strs):
        anagrams = collections.defaultdict(list)

        for string in strs:
            key = ''.join(sorted(string))
            anagrams[key].append(string)

        return list(anagrams.values())

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    input_strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result1 = solution.groupAnagrams(input_strs1)
    print("Test Case 1:", result1)
    
    # Test case 2
    input_strs2 = ["listen", "silent", "enlist"]
    result2 = solution.groupAnagrams(input_strs2)
    print("Test Case 2:", result2)

