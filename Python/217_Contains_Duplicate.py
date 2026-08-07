"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:
    Input: nums = [1,2,3,1]
    Output: true
    Explanation:
        The element 1 occurs at the indices 0 and 3.

Example 2:
    Input: nums = [1,2,3,4]
    Output: false
    Explanation:
        All elements are distinct.

Example 3:
    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

Constraints:
    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
"""
from typing import List

class Solution:
    
    # def containsDuplicate_BruteForce(self, nums: List[int]) -> bool:
    #     """
    #     Brute force approach: Check each element with every other element
    #     Time Complexity: O(n^2)
    #     Space Complexity: O(1)
    #     """
    #     if len(nums) == 1:
    #         # print(f"Length of nums: {len(nums)}")
    #         return False
    #     else:
    #         for k, v in enumerate(nums):
    #             # print(nums[k+1:])
    #             for j in nums[k+1:]:
    #                 # print(nums[k:])
    #                 if v == j:
    #                     return True
    #         return False
        
    # def containsDuplicate_SortedArray(self, nums: List[int]) -> bool:
    #     """
    #     Sorting approach: Sort the list of elements by ascending order, then check.
    #     Time Complexity: O(nlogn)
    #     Space Complexity: O(1)
    #     """
    #     if len(nums) == 1:
    #         return False
    #     else:
    #         # Added a Sorting Function to sort the list by ascending value.
    #         nums_sorted = sorted(nums)

    #         for k, v in enumerate(nums_sorted):
    #             print(nums_sorted[k+1:])
    #             for j in nums_sorted[k+1:]:
    #                 print(nums[k:])
    #                 print(v, j)
    #                 if v == j:
    #                     return True
    #         return False
        
    def containsDuplicate_Hashmap(self, nums: List[int]) -> bool:
        """
        Hashset Approach: Stores the value in a hashset which allows for O(1) lookup.
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        if len(nums) == 1:
            return False
        else:
            Hashset = set()
            for i in nums:
                if i not in Hashset:
                    Hashset.add(i)
                else:
                    return True
            return False  

def main():
    sol = Solution()
    nums = [1 ,3, 2, 4, 1]
    ans = sol.containsDuplicate_Hashmap(nums)
    print(f"Answer: {ans}")

if __name__ == "__main__":
    main()