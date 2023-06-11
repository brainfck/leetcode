#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prevMap:
                return [prevMap[diff], i]
            else:
                prevMap[nums[i]] = i
# @lc code=end

