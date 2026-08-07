"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

## Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

## Example 2:
Input: s = "rat", t = "car"
Output: false

## Constraints:
    1. 1 <= s.length, t.length <= 5 * 104
    2. s and t consist of lowercase English letters.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # First check if their length is NOT the same (Easiest Check)
        if len(s) != len(t):
            return False

        # Use the set to get each unique character
        s_let = set(s)
        t_set = set(t)

        # Check if the count of each unique character matches in each set.
        for i in s_let:
            # count the num of times unique character `i` appeared in each string.
            char_count_s = s.count(i)
            char_count_t = t.count(i)

            if char_count_s != char_count_t:
                return False

        return True
        

def main():
    sol = Solution()
    s = "anagram"
    t = "nagaram"
    ans = sol.isAnagram(s, t)
    print(f"Answer: {ans}")

if __name__ == "__main__":
    main()