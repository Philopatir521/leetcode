#
# @lc app=leetcode id=1929 lang=python3
#
# [1929] Concatenation of Array
#

# @lc code=start
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int])-> List[int]:
        n = len(nums)
        ans = [0]*(2*n)
        for i ,  num in enumerate(nums):
            ans[i] =ans[i+n] = num
        return ans
# @lc code=end

