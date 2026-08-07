"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        str_dict: dict[int,str] = {}
        result = []
        similar: dict[str,List[str]] = {}

        # Creates a Dict of the List with the Strings sorted.
        for idx, str in enumerate(strs):
            str_dict[idx] = ''.join(sorted(str))
        
        # Converts the Dict into a List so that you use For Loop for it.
        for k,v in str_dict.items():
            # If the value (e.g. 'aet') is not in the Dict, 
            # Add the String of the Index of the value as the new Value, 
            # The old Value is the new Key.
            #
            # Else append the String to the value of the key.

            if v not in similar:
                similar[v] = [strs[k]]
            else:
                similar[v].append(strs[k])
        
        # Create the Result List from the Dict.
        for k,v in similar.items():
            result.append(v)

        return result

def main():
    sol = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    ans = sol.groupAnagrams(strs)
    print(f"Answer: {ans}")

if __name__ == "__main__":
    main()