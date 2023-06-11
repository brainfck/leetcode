#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        dict = {}
        
        for c in s:
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1
        
        for c in t:
            if c in dict:
                dict[c] -= 1
            else:
                return False
        
        for key in dict:
            if dict[key] < 0: return False
        
        return True
# @lc code=end